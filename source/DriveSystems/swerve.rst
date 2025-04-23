Swerve Chassis Tutorial
=======================


The swerve chassis is one of the most advanced drivetrains in FRC, offering exceptional speed, power, and maneuverability, which is why it’s commonly used by top-tier teams. However, it requires the most tuning and debugging to achieve optimal performance.

Swerve chassis image below:

.. image:: https://www.chiefdelphi.com/uploads/default/98c9352ca78c34dfdc08f8b46b30b17e24915dd6
    :alt: Swerve Chassis Image

and its kinematics

.. image:: https://compendium.readthedocs.io/en/latest/_images/swerve.png
    :alt: Swerve Drive Kinematics Image

+++++++++++++++++++++++++
Swerve Chassis Dependices
+++++++++++++++++++++++++

| 8 motors (4 wheels, 2 motors per module)
| 4 encoders (1 per module, usually use CANCoder)
| 1 gyro (1 per robot)

.. note:: 
    If you use all CTRE products (kraken motor, cancoder, pigeon), you can unlock hidden feature called Swerve Project Generator in Phoenix Tuner X 

.. tip:: 
    Swerve drive code is more complex compared to the other two chassis types, so here's a `GitHub example <https://github.com/FRC-8569/SwerveChassisExample>`_ to help you get started.


++++++++++++++++++++
Constants Definition
++++++++++++++++++++

There's two motors per wheel, one is for drive and one is for rotate, so we can define our chassis constants as

.. caution:: 
    Here we use front back ... to perform modules, in real programming, recommend to use mod0, mod1 to name the modules
    or you can check your gyro definition to know your robot facing.


.. tabs::
    .. tab:: SwerveChassisMotorID
        .. code-block::

            public class SwerveConstants{
                public static final int FrontLeftDriveID = 0;
                public static final int FrontLeftRotationID = 0;
                
                public static final int FrontRightDriveID = 0;
                public static final int FrontRightRotationID = 0;

                public static final int BackLeftDriveID = 0;
                public static final int BackLeftRotationID = 0;

                public static final int BackRightDriveID = 0;
                public static final int BackRightRotationID = 0;

                public static final int FrontLeftCANCoderID = 0;
                public static final int FrontRightCANCoderID = 0;
                public static final int BackLeftCANCoderID = 0;
                public static final int BackRightCANCoderID = 0;

                public static final double FrontLeftCANCoderOffset = 0;
                public static final double FrontRightCANCoderOffset = 0;
                public static final double BackLeftCANCoderOffset = 0;
                public static final double BackRightCANCoderOffset = 0;
            }

.. attention:: 
    The CANCoder is not always percise for our robot, so we need to calibrate the CANCoder by :ref:`CANCoder-Calibration`

Module Position Definition
++++++++++++++++++++++++++

we need to create a SwerveKinematics

.. tabs::
    .. tab:: SwerveKinematics
        .. code-block:: java

            /*                 ^
            |<-----WIDTH------>|
                               |
                             LENGTH
                               |
                               |
                               ^
            */
            public static final SwerveDriveKinematics kSwerveKinematics = new SwerveDriveKinematics(
                new Translation2d(LENGTH/2, WIDTH/2),
                new Translation2d(LENGTH/2, -WIDTH/2),
                new Translation2d(-LENGTH/2, WIDTH/2),
                new Translation2d(-LENGTH/2, -WIDTH/2)
            );

to tell robot where the module is.

.. note:: 
    You can use self-rotation to test whether your location settings are incorrect. Aside from incorrect CANCoder offsets, you can often fix the issue by adjusting the signs (e.g., modifying '-' values).
    If your robot forms an X-shape or rotates in the wrong direction, it's likely due to incorrect location definitions.

and define other constants we need

.. tabs::
    .. tab:: OtherConstants
        .. code-block:: java

            public static final double kMaxMotorSpeedRPS = 5676/60; //NEO Motor Free Speed
            public static final double kDrivePositionConversionFactor = 1/ChassisConstants.kDriveGearRatio*ChassisConstants.kWheelDiameter*Math.PI;
            public static final double kDriveVelocityConversionFactor = kDrivePositionConversionFactor/60;
            public static final double kMotorKv = 476; //search from https://docs.revrobotics.com/brushless/neo/v1.1
            public static final double kMaxRobotSpeedMPS = kMaxMotorSpeedRPS/ChassisConstants.kDriveGearRatio*ChassisConstants.kWheelDiameter*Math.PI; //calculate the maximum velocity of the robot
        
after finish defining the constants, we can dive into the swerve module programming

**Swerve Moudle Programming**

.. tabs::
    .. tab:: SparkMax+NEO
        .. code-block:: java

            import com.ctre.phoenix6.configs.CANcoderConfiguration;
            import com.ctre.phoenix6.hardware.CANcoder;
            import com.ctre.phoenix6.signals.SensorDirectionValue;
            import com.revrobotics.RelativeEncoder;
            import com.revrobotics.spark.SparkClosedLoopController;
            import com.revrobotics.spark.SparkMax;
            import com.revrobotics.spark.SparkBase.ControlType;
            import com.revrobotics.spark.SparkBase.PersistMode;
            import com.revrobotics.spark.SparkBase.ResetMode;
            import com.revrobotics.spark.SparkLowLevel.MotorType;
            import com.revrobotics.spark.config.SparkMaxConfig;
            import com.revrobotics.spark.config.SparkBaseConfig.IdleMode;

            import edu.wpi.first.math.controller.PIDController;
            import edu.wpi.first.math.geometry.Rotation2d;
            import edu.wpi.first.math.kinematics.SwerveModulePosition;
            import edu.wpi.first.math.kinematics.SwerveModuleState;
            import frc.robot.Constants.ChassisConstants;
            import frc.robot.Constants.MotorConstants;
            import frc.robot.Constants.PIDValues;

            public class SwerveMod {
                public SparkMax DriveMotor, RotationMotor; //Two motors
                public RelativeEncoder DriveEncoder; // You can get various values from the encoder like velocity, position etc.
                public CANcoder cancoder; //CTRE CANCoder
                public SparkClosedLoopController DrivePID; //Driving PID control for smoothen drive
                public PIDController RotationPID; //Rotation PID for facing tuning
                public CANcoderConfiguration cancoderConfig; //CANCoder configuration
                public SparkMaxConfig Driveconfig, RotationConfig; // Motor Configuration


                public SwerveMod(int DriveMotorID, int RotationMotorID, int CANCoderID, double CANCoderOffset){
                    //initial the item we just defined
                    DriveMotor = new SparkMax(DriveMotorID, MotorType.kBrushless);
                    RotationMotor = new SparkMax(RotationMotorID, MotorType.kBrushless);
                    cancoder = new CANcoder(CANCoderID);

                    cancoderConfig = new CANcoderConfiguration();
                    Driveconfig = new SparkMaxConfig();
                    RotationConfig = new SparkMaxConfig();

                    Driveconfig
                        .idleMode(IdleMode.kBrake)
                        .inverted(false);
                    //closedloop means PID control, not required but you can smoothen your drive when applied.
                    Driveconfig.closedLoop
                        .pidf(PIDValues.DrivePID[0], PIDValues.DrivePID[1], PIDValues.DrivePID[2], PIDValues.DrivePID[3])
                        .outputRange(-1, 1);

                    //configure the encoder
                    Driveconfig.encoder
                        .positionConversionFactor(MotorConstants.kDrivePositionConversionFactor)
                        .velocityConversionFactor(MotorConstants.kDriveVelocityConversionFactor);

                    RotationConfig
                        .idleMode(IdleMode.kBrake)
                        .inverted(true);
                    RotationConfig.encoder
                        .positionConversionFactor(MotorConstants.kDrivePositionConversionFactor)
                        .velocityConversionFactor(MotorConstants.kDriveVelocityConversionFactor);

                    cancoderConfig.MagnetSensor
                        .withSensorDirection(SensorDirectionValue.CounterClockwise_Positive)
                        .withMagnetOffset(CANCoderOffset);


                    //apply the motor settings to the motor
                    DriveMotor.configure(Driveconfig, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters);
                    RotationMotor.configure(RotationConfig, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters);
                    cancoder.getConfigurator().apply(cancoderConfig); //applying settings to CANCoder

                    DriveEncoder = DriveMotor.getEncoder();//get encoder from motor
                    RotationPID = new PIDController(PIDValues.RotationPID[0], PIDValues.RotationPID[1], PIDValues.RotationPID[2]);//Define a PID controller for rotation
                    DrivePID = DriveMotor.getClosedLoopController();// get drive hardware PID controller
                }

                //get the module current state (v, θ) in (m/s, deg)
                public SwerveModuleState getState(){
                    return new SwerveModuleState(
                        DriveEncoder.getVelocity(),
                        Rotation2d.fromDegrees(cancoder.getPosition().getValueAsDouble())
                    );
                }

                //get the module position for odometry in (p, θ) of (m, deg)
                public SwerveModulePosition getPosition(){
                    return new SwerveModulePosition(
                        DriveEncoder.getPosition(),
                        Rotation2d.fromDegrees(cancoder.getPosition().getValueAsDouble())
                    );
                }

                //set the module state to the desired state
                public void setState(SwerveModuleState state){
                    state.optimize(getState().angle);
                    DrivePID.setReference(mpsToRPM(state.speedMetersPerSecond), ControlType.kVelocity);
                    RotationMotor.set(
                        RotationPID.calculate(
                            Rotation2d.fromRotations(cancoder.getAbsolutePosition().getValueAsDouble()).getDegrees(),
                            state.angle.getDegrees())
                    );
                }

                //converter
                public double mpsToRPM(double mps){
                    return (mps*60)/(ChassisConstants.kWheelDiameter*Math.PI)*ChassisConstants.kDriveGearRatio;
                }
            }

and then is the chasis code.

.. tabs::
    .. tab:: SparkMax+NEO
        .. code-block:: java

            import com.studica.frc.AHRS;
            import com.studica.frc.AHRS.NavXComType;

            import edu.wpi.first.math.geometry.Pose2d;
            import edu.wpi.first.math.kinematics.ChassisSpeeds;
            import edu.wpi.first.math.kinematics.SwerveDriveKinematics;
            import edu.wpi.first.math.kinematics.SwerveDriveOdometry;
            import edu.wpi.first.math.kinematics.SwerveModulePosition;
            import edu.wpi.first.math.kinematics.SwerveModuleState;
            import edu.wpi.first.networktables.NetworkTableInstance;
            import edu.wpi.first.networktables.PubSubOption;
            import edu.wpi.first.networktables.StructArrayPublisher;
            import edu.wpi.first.networktables.StructPublisher;
            import edu.wpi.first.wpilibj2.command.SubsystemBase;
            import frc.robot.Constants.ChassisConstants;
            import frc.robot.Constants.MotorConstants;

            public class SwerveChassis extends SubsystemBase{
                public SwerveMod LeftFront, RightFront, LeftBack, RightBack; //Define the modules
                public AHRS gyro;
                public SwerveDriveOdometry odometry;
                public StructArrayPublisher<SwerveModuleState> statePublish; //For AdvantageScope (Data publishing)
                public StructPublisher<Pose2d> odometryPublish; //and also this line

                public SwerveChassis(){

                    //Initialize the items
                    LeftFront = new SwerveMod(
                        MotorConstants.LeftFrontDriveID, 
                        MotorConstants.LeftFrontRotationID, 
                        MotorConstants.LeftFrontCANCoderID, 
                        MotorConstants.LeftFrontOffset);

                    LeftBack = new SwerveMod(
                        MotorConstants.LeftBackDriveID, 
                        MotorConstants.LeftBackRotationID, 
                        MotorConstants.LeftBackCANCoderID , 
                        MotorConstants.LeftBackOffset);

                    RightFront = new SwerveMod(
                        MotorConstants.RightFrontDriveID, 
                        MotorConstants.RightFrontRotationID, 
                        MotorConstants.RightFrontCANCoderID, 
                        MotorConstants.RightFrontOffset);

                    RightBack = new SwerveMod(
                        MotorConstants.RightBackRotationID, 
                        MotorConstants.RightBackRotationID, 
                        MotorConstants.RightBackCANCoderID, 
                        MotorConstants.RightBackOffset);

                    gyro = new AHRS(NavXComType.kMXP_SPI);
                    odometry = new SwerveDriveOdometry(ChassisConstants.kSwerveDriveKinematics, gyro.getRotation2d(), getModulePosition());
                    statePublish = NetworkTableInstance.getDefault().getStructArrayTopic("SwerveDrive",SwerveModuleState.struct).publish(PubSubOption.keepDuplicates(false));
                    odometryPublish = NetworkTableInstance.getDefault().getStructTopic("Odometry", Pose2d.struct).publish(PubSubOption.keepDuplicates(false));
                }

                //drive the chassis from the double value input
                public void drive(double xSpeed, double ySpeed, double zRotation){
                    setModuleState(
                        ChassisConstants.kSwerveDriveKinematics.toSwerveModuleStates(
                            ChassisSpeeds.fromRobotRelativeSpeeds(ChassisSpeeds.discretize(new ChassisSpeeds(xSpeed, ySpeed, zRotation), 0.02), gyro.getRotation2d())
                        )
                    );
                }

                //receive the module states from the SwerveModuleStates and apply to each module
                public void setModuleState(SwerveModuleState[] states){
                    SwerveDriveKinematics.desaturateWheelSpeeds(states, MotorConstants.kMaxRobotSpeedMPS);
                    LeftFront.setState(states[0]);
                    RightFront.setState(states[1]);
                    LeftBack.setState(states[2]);
                    RightBack.setState(states[3]);
                }

                //get the module positions
                public SwerveModulePosition[] getModulePosition(){
                    return new SwerveModulePosition[]{
                        LeftFront.getPosition(),
                        RightFront.getPosition(),
                        LeftBack.getPosition(),
                        RightBack.getPosition()
                    };
                }

                public SwerveModuleState[] getModuleStates(){
                    return new SwerveModuleState[]{
                        LeftFront.getState(),
                        RightFront.getState(),
                        LeftBack.getState(),
                        RightBack.getState()
                    };
                }

                //upload the data to the NetworkTables
                @Override
                public void periodic(){
                    odometry.update(gyro.getRotation2d(), getModulePosition());
                    odometryPublish.set(odometry.getPoseMeters());
                    statePublish.set(this.getModuleStates());
                }
            }


.. _CANCoder-Calibration:

CANCoder Calibration
++++++++++++++++++++

1. Frist of all, set the CANCoderOffset to Zero and motor to coast.
2. Deploy the code.
3. Then make the wheel's gear facing the same direction (rotate in same method like all clockwise or counter clockwise)
4. Use a straight thing like aluminum tube to alignment the wheels
5. copy the value CANCoder read to the CANCoderOffset and set motor to brake

.. note:: the value need to times -1

deploy the code
and enable the robot, it will rotate the motor to the same direction if offset has no critical error.