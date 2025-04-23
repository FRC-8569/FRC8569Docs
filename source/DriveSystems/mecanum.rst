Mecanum Chassis tutorial
========================

The mecanum chassis serves as a transition between the KOP and swerve drivetrains. It offers greater driving flexibility with only a small amount of additional code compared to the KOP chassis.

Mecanum chassis image below:

.. image:: https://d2t1xqejof9utc.cloudfront.net/screenshots/pics/1ab60f73d81dad6e74c83b6ad6e429e8/large.png
    :alt: Mecanum Chassis

You can also use the motors from the `KOP <KOP.html>`_ here — now let's check out the driving kinematics.

Because of the characteristics of the mecanum wheel, the robot can perform more complex movements, such as x-y panning and driving while rotating like the image below.

.. image:: https://upload.wikimedia.org/wikipedia/commons/c/c4/Mecanum_wheel_control_principle.svg
    :alt: Mecanum Drive kinematics

.. tip:: 
    If you want to know more about mecanum drive kinematics, you can check out `this <https://www.youtube.com/watch?v=hoTK9CZBnaE>`_ video.


This image demonstrates how the chassis responds to various wheel spin patterns. Each wheel's motion can be described as:

.. tabs::
    .. tab:: Wheel Speeds
        .. code-block:: java

            FrontLeft = Vx + Vy + rotation
            FrontRight = Vx - Vy - rotation
            BackLeft = Vx - Vy + rotation
            BackRight = Vx + Vy - rotation

and below the chassis code

**OFFICAL METHOD**

.. tabs::
    .. tab:: SparkMax+NEO
        .. code-block:: java
                    
            import com.revrobotics.spark.SparkMax;
            import com.revrobotics.spark.SparkLowLevel.MotorType;
            import com.revrobotics.spark.config.SparkMaxConfig;
            import com.revrobotics.spark.config.SparkBaseConfig.IdleMode;

            import edu.wpi.first.wpilibj.drive.MecanumDrive;
            import edu.wpi.first.wpilibj2.command.SubsystemBase;
            import frc.robot.Constants.ChassisConstants;
            
            public class NEOChassis extends SubsystemBase{
                public SparkMax LeftFrontMotor, RightFrontMotor, LeftBackMotor, RightBackMotor;
                public SparkMaxConfig LeftFrontConfig, RightFrontConfig, LeftBackConfig, RightBackConfig;

                public MecanumDrive drive;

                public NEOChassis(){
                    LeftFrontMotor = new SparkMax(ChassisConstants.FrontLeftMotor, MotorType.kBrushless);
                    RightFrontMotor = new SparkMax(ChassisConstants.FrontRightMotor, MotorType.kBrushless);
                    LeftBackMotor = new SparkMax(ChassisConstants.BackLeftMotor, MotorType.kBrushless);
                    RightBackMotor = new SparkMax(ChassisConstants.BackRightMotor, MotorType.kBrushless);

                    LeftFrontConfig = new SparkMaxConfig();
                    RightFrontConfig = new SparkMaxConfig();
                    LeftBackConfig = new SparkMaxConfig();
                    RightBackConfig = new SparkMaxConfig();

                    LeftFrontConfig
                        .idleMode(IdleMode.kBrake)
                        .inverted(false);
                    
                    LeftBackConfig
                        .idleMode(IdleMode.kBrake)
                        .inverted(false);

                    RightFrontConfig
                        .idleMode(IdleMode.kBrake)
                        .inverted(true);

                    RightBackConfig
                        .idleMode(IdleMode.kBrake)
                        .inverted(true);

                    drive = new MecanumDrive(LeftFrontMotor, LeftBackMotor, RightFrontMotor, RightBackMotor);
                }
            }

    .. tab:: TalonSRX+CIM
        .. code-block:: java

            import com.ctre.phoenix.motorcontrol.NeutralMode;
            import com.ctre.phoenix.motorcontrol.can.WPI_TalonSRX;

            import edu.wpi.first.wpilibj.drive.MecanumDrive;
            import frc.robot.Constants.ChassisConstants;

            public class CIMChassis {
                public WPI_TalonSRX FrontLeft, FrontRight, BackLeft, BackRight;
                public MecanumDrive drive;

                public CIMChassis(){
                    FrontLeft = new WPI_TalonSRX(ChassisConstants.FrontLeftMotor);
                    FrontRight = new WPI_TalonSRX(ChassisConstants.FrontRightMotor);
                    BackLeft = new WPI_TalonSRX(ChassisConstants.BackLeftMotor);                        BackRight = new WPI_TalonSRX(ChassisConstants.BackRightMotor);

                    FrontLeft.setNeutralMode(NeutralMode.Brake);
                    FrontLeft.setInverted(false);

                    BackLeft.setNeutralMode(NeutralMode.Brake);
                    FrontRight.setInverted(false);

                    FrontRight.setNeutralMode(NeutralMode.Brake);
                    FrontRight.setInverted(true);

                    BackRight.setNeutralMode(NeutralMode.Brake);
                    BackRight.setInverted(true);

                    drive = new MecanumDrive(FrontLeft, BackLeft, FrontRight, BackRight);
                }
            }



**SELF WRITTEN METHOD**

.. tabs::
    .. tab:: SparkMax+NEO
        .. code-block:: java

            import com.revrobotics.spark.SparkMax;
            import com.revrobotics.spark.SparkLowLevel.MotorType;
            import com.revrobotics.spark.config.SparkMaxConfig;
            import com.revrobotics.spark.config.SparkBaseConfig.IdleMode;

            import edu.wpi.first.wpilibj2.command.SubsystemBase;
            import frc.robot.Constants.ChassisConstants;

            public class NEOChassis extends SubsystemBase{
                public SparkMax LeftFrontMotor, RightFrontMotor, LeftBackMotor, RightBackMotor;
                public SparkMaxConfig LeftFrontConfig, RightFrontConfig, LeftBackConfig, RightBackConfig;

                public NEOChassis(){
                    LeftFrontMotor = new SparkMax(ChassisConstants.FrontLeftMotor, MotorType.kBrushless);
                    RightFrontMotor = new SparkMax(ChassisConstants.FrontRightMotor, MotorType.kBrushless);
                    LeftBackMotor = new SparkMax(ChassisConstants.BackLeftMotor, MotorType.kBrushless);
                    RightBackMotor = new SparkMax(ChassisConstants.BackRightMotor, MotorType.kBrushless);

                    LeftFrontConfig = new SparkMaxConfig();
                    RightFrontConfig = new SparkMaxConfig();
                    LeftBackConfig = new SparkMaxConfig();
                    RightBackConfig = new SparkMaxConfig();

                    LeftFrontConfig
                        .idleMode(IdleMode.kBrake)
                        .inverted(false);
                    
                    LeftBackConfig
                        .idleMode(IdleMode.kBrake)
                        .inverted(false);

                    RightFrontConfig
                        .idleMode(IdleMode.kBrake)
                        .inverted(true);

                    RightBackConfig
                        .idleMode(IdleMode.kBrake)
                        .inverted(true);

                }

                public void drive(double Vx, double Vy, double rotation){
                    LeftFrontMotor.set(Vx+Vy+rotation);
                    LeftBackMotor.set(Vx-Vy+rotation);
                    RightFrontMotor.set(Vx-Vy-rotation);
                    RightBackMotor.set(Vx+Vy-rotation);
                }
            }

    .. tab:: TalonSRX+CIM
        .. code-block:: java

            import com.ctre.phoenix.motorcontrol.ControlMode;
            import com.ctre.phoenix.motorcontrol.NeutralMode;
            import com.ctre.phoenix.motorcontrol.TalonSRXControlMode;
            import com.ctre.phoenix.motorcontrol.can.TalonSRX;

            import edu.wpi.first.wpilibj.drive.MecanumDrive;
            import frc.robot.Constants.ChassisConstants;

            public class CIMChassis {
                public TalonSRX FrontLeft, FrontRight, BackLeft, BackRight;
                public MecanumDrive drive;

                public CIMChassis(){
                    FrontLeft = new TalonSRX(ChassisConstants.FrontLeftMotor);
                    FrontRight = new TalonSRX(ChassisConstants.FrontRightMotor);
                    BackLeft = new TalonSRX(ChassisConstants.BackLeftMotor);
                    BackRight = new TalonSRX(ChassisConstants.BackRightMotor);

                    FrontLeft.setNeutralMode(NeutralMode.Brake);
                    FrontLeft.setInverted(false);

                    BackLeft.setNeutralMode(NeutralMode.Brake);
                    FrontRight.setInverted(false);

                    FrontRight.setNeutralMode(NeutralMode.Brake);
                    FrontRight.setInverted(true);

                    BackRight.setNeutralMode(NeutralMode.Brake);
                    BackRight.setInverted(true);
                }

                public void drive(double xSpeed, double ySpeed, double zRotation){
                    FrontLeft.set(TalonSRXControlMode.PercentOutput, xSpeed+ySpeed+zRotation);
                    BackLeft.set(TalonSRXControlMode.PercentOutput, xSpeed-ySpeed+zRotation);
                    FrontRight.set(ControlMode.PercentOutput, xSpeed-ySpeed-zRotation);
                    BackRight.set(ControlMode.PercentOutput, xSpeed+ySpeed-zRotation);
                }
            }
    
    .. tab:: Kraken
        .. code-block:: java
            
            import com.ctre.phoenix6.configs.TalonFXConfiguration;
            import com.ctre.phoenix6.hardware.TalonFX;
            import com.ctre.phoenix6.signals.InvertedValue;
            import com.ctre.phoenix6.signals.NeutralModeValue;

            import frc.robot.Constants.ChassisConstants;

            public class KrakenChassis {
                public TalonFX FrontLeft, FrontRight, BackLeft, BackRight;
                public TalonFXConfiguration FrontLeftConfig, FrontRightConfig, BackLeftConfig, BackRightConfig;

                public KrakenChassis(){
                    FrontLeft = new TalonFX(ChassisConstants.FrontLeftMotor);
                    FrontRight = new TalonFX(ChassisConstants.FrontRightMotor);
                    BackLeft = new TalonFX(ChassisConstants.BackLeftMotor);
                    BackRight = new TalonFX(ChassisConstants.BackRightMotor);

                    FrontLeftConfig = new TalonFXConfiguration();
                    FrontRightConfig = new TalonFXConfiguration();
                    BackLeftConfig = new TalonFXConfiguration();
                    BackRightConfig = new TalonFXConfiguration();

                    FrontLeftConfig.MotorOutput
                        .withInverted(InvertedValue.Clockwise_Positive)
                        .withNeutralMode(NeutralModeValue.Brake);
                    
                    BackLeftConfig.MotorOutput
                        .withInverted(InvertedValue.Clockwise_Positive)
                        .withNeutralMode(NeutralModeValue.Brake);

                    FrontRightConfig.MotorOutput
                        .withInverted(InvertedValue.CounterClockwise_Positive)
                        .withNeutralMode(NeutralModeValue.Brake);

                    BackRightConfig.MotorOutput
                        .withInverted(InvertedValue.CounterClockwise_Positive)
                        .withNeutralMode(NeutralModeValue.Brake);
                    

                    FrontLeft.getConfigurator().apply(FrontLeftConfig);
                    BackLeft.getConfigurator().apply(BackLeftConfig);
                    FrontRight.getConfigurator().apply(FrontRightConfig);
                    BackRight.getConfigurator().apply(BackRightConfig);
                }
            }

.. note:: 
    Check out the references
    `MecanumDrive <https://docs.wpilib.org/en/stable/docs/software/hardware-apis/motors/wpi-drive-classes.html#using-the-mecanumdrive-class-to-control-mecanum-drive-robots>`_