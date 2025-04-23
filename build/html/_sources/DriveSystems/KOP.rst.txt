KOP Chassis Tutorial
====================

The KOP chassis is the easiest option for building and programming in FRC, which makes it perfect for new teams—simple design, strong build, and barely any code needed.

KOP chassis image below:

.. image:: https://cdn.andymark.com/product_images/am14u5-6-wheel-drop-center-robot-drive-base-first-kit-of-parts-chassis/61cdd905b8a4235a6564320c/zoom.jpg
    :alt: KOP Chassis

In this image, each side has three wheels powered by two motors. The motors allow the robot to move forward and backward, and by varying the speed between the two sides, you can make it turn.

You can program your KOP chassis in this method:

Software Installation:
    SparkMax + NEO v1.1:
        Software VendorDeps: REVLib

    TalonSRX + CIM:
        Software VendorDeps: Phoneix 5

    TalonFX (Kraken):
        Software VendorDeps: Phoneix 6

.. note:: 
    You don't need to type out the entire name—just start typing, wait for the recommended words to appear, and hit Enter to fill it out and auto imported when needed.


.. !TODO: Kraken Self Written Chassis
**OFFICAL DRIVE METHOD**

.. tabs::
    .. tab:: SparkMax+NEO
            .. code-block:: java

                //Chassis.java
                import com.revrobotics.spark.SparkMax;
                import com.revrobotics.spark.SparkBase.PersistMode;
                import com.revrobotics.spark.SparkBase.ResetMode;
                import com.revrobotics.spark.SparkLowLevel.MotorType;
                import com.revrobotics.spark.config.SparkMaxConfig;
                import com.revrobotics.spark.config.SparkBaseConfig.IdleMode;

                import edu.wpi.first.wpilibj.drive.DifferentialDrive;
                import edu.wpi.first.wpilibj2.command.SubsystemBase;
                import frc.robot.Constants.ChassisConstants;

                //the file name must same with this
                //              ^
                //              |
                public class NEOChassis extends SubsystemBase{
                    public SparkMax LeftMotor, RightMotor; //Define the motors from the motor controller (define four motors if you use four)
                    public SparkMaxConfig LeftConfig, RightConfig; //Define the configuration of the motors
                    public DifferentialDrive drive; //The driving method provided from WPILib

                    public NEOChassis(){
                        //Initialize the item we just defined
                        LeftMotor = new SparkMax(ChassisConstants.LeftMotorID, MotorType.kBrushless);//use kBrushless because the NEO v1.1 motor is the brushless motor
                        RightMotor = new SparkMax(ChassisConstants.RightMotorID, MotorType.kBrushless);

                        LeftConfig = new SparkMaxConfig();
                        RightConfig = new SparkMaxConfig();

                        
                        LeftConfig
                            .idleMode(IdleMode.kBrake)
                            .inverted(false);
                        RightConfig
                            .idleMode(IdleMode.kBrake)
                            .inverted(true); // You need to invert the motor; otherwise, it will spin in the wrong direction when driving straight.

                        LeftMotor.configure(LeftConfig, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters); //Apply the configurations
                        RightMotor.configure(RightConfig, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters);//Both choose yes for the less problems, it will factory reset the motor
                        
                        drive = new DifferentialDrive(LeftMotor, RightMotor); //look, it's so easy, right?
                    }
                }


    .. tab:: TalonSRX+CIM
            .. code-block:: java

                    //Chassis.java
                    import com.ctre.phoenix.motorcontrol.InvertType;
                    import com.ctre.phoenix.motorcontrol.NeutralMode;
                    import com.ctre.phoenix.motorcontrol.can.TalonSRXConfiguration;
                    import com.ctre.phoenix.motorcontrol.can.WPI_TalonSRX;

                    import edu.wpi.first.wpilibj.drive.DifferentialDrive;
                    import edu.wpi.first.wpilibj2.command.SubsystemBase;
                    import frc.robot.Constants.ChassisConstants;


                    //File name must same with this
                    //              ^
                    //              |
                    public class CIMChassis extends SubsystemBase{
                        public WPI_TalonSRX LeftMotor, RightMotor; //Define two motors, you can define four if you needed
                        public DifferentialDrive drive; //Define the drive method provided from the WPILib

                        public CIMChassis(){
                            //Initialize the items we just defined
                            LeftMotor = new WPI_TalonSRX(ChassisConstants.LeftMotorID);
                            RightMotor = new WPI_TalonSRX(ChassisConstants.RightMotorID);

                            //reset the motor configuration for the less bugs
                            LeftMotor.configAllSettings(new TalonSRXConfiguration());
                            RightMotor.configAllSettings(new TalonSRXConfiguration());


                            LeftMotor.setNeutralMode(NeutralMode.Brake);
                            LeftMotor.setInverted(InvertType.None);

                            RightMotor.setNeutralMode(NeutralMode.Brake);
                            RightMotor.setInverted(InvertType.InvertMotorOutput);

                            drive = new DifferentialDrive(LeftMotor, RightMotor);
                        }
                    }
.. tip:: 
    It's recommended to write your own drive method instead of using the official one, as it offers more flexibility and extensibility for your drive system.
.. danger:: 
    Make sure to use either the official drive method or your own properly written one; otherwise, it could cause runtime errors.

**SELF WRITEEN METHOD**

.. tabs::
    .. tab:: SparkMax+NEO
        .. code-block:: java
                        
            import com.revrobotics.spark.SparkMax;
            import com.revrobotics.spark.SparkBase.PersistMode;
            import com.revrobotics.spark.SparkBase.ResetMode;
            import com.revrobotics.spark.SparkLowLevel.MotorType;
            import com.revrobotics.spark.config.SparkMaxConfig;
            import com.revrobotics.spark.config.SparkBaseConfig.IdleMode;

            import edu.wpi.first.wpilibj2.command.SubsystemBase;
            import frc.robot.Constants.ChassisConstants;

            //the file name must same with this
            //              ^
            //              |
            public class NEOChassis extends SubsystemBase{
                public SparkMax LeftMotor, RightMotor; //Define the motors from the motor controller (define four motors if you use four)
                public SparkMaxConfig LeftConfig, RightConfig; //Define the configuration of the motors

                public NEOChassis(){
                    //Initialize the item we just defined
                    LeftMotor = new SparkMax(ChassisConstants.LeftMotorID, MotorType.kBrushless);//use kBrushless because the NEO v1.1 motor is the brushless motor
                    RightMotor = new SparkMax(ChassisConstants.RightMotorID, MotorType.kBrushless);

                    LeftConfig = new SparkMaxConfig();
                    RightConfig = new SparkMaxConfig();

                    
                    LeftConfig
                        .idleMode(IdleMode.kBrake)
                        .inverted(false);
                    RightConfig
                        .idleMode(IdleMode.kBrake)
                        .inverted(true); // You need to invert the motor; otherwise, it will spin in the wrong direction when driving straight.

                    LeftMotor.configure(LeftConfig, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters); //Apply the configurations
                    RightMotor.configure(RightConfig, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters);//Both choose yes for the less problems, it will factory reset the motor
                }

                public void drive(double speed, double rotation){
                    LeftMotor.set(speed+rotation);
                    RightMotor.set(speed-rotation);
                }

    .. tab:: TalonSRX+CIM
        .. code-block:: java

            import com.ctre.phoenix.motorcontrol.InvertType;
            import com.ctre.phoenix.motorcontrol.NeutralMode;
            import com.ctre.phoenix.motorcontrol.can.TalonSRX;
            import com.ctre.phoenix.motorcontrol.can.TalonSRXConfiguration;

            import edu.wpi.first.wpilibj2.command.SubsystemBase;
            import frc.robot.Constants.ChassisConstants;


            //File name must same with this
            //              ^
            //              |
            public class CIMChassis extends SubsystemBase{
                public TalonSRX LeftMotor, RightMotor; //Define two motors, you can define four if you needed
                
                public CIMChassis(){
                    //Initialize the items we just defined
                    LeftMotor = new TalonSRX(ChassisConstants.LeftMotorID);
                    RightMotor = new TalonSRX(ChassisConstants.RightMotorID);

                    //reset the motor configuration for the less bugs
                    LeftMotor.configAllSettings(new TalonSRXConfiguration());
                    RightMotor.configAllSettings(new TalonSRXConfiguration());


                    LeftMotor.setNeutralMode(NeutralMode.Brake);
                    LeftMotor.setInverted(InvertType.None);

                    RightMotor.setNeutralMode(NeutralMode.Brake);
                    RightMotor.setInverted(InvertType.InvertMotorOutput);
                }

                public void drive(double speed, double rotation){
                    LeftMotor.set(ControlMode.PercentOutput, speed+rotation);
                    RightMotor.set(ControlMode.PercentOutput, speed-rotation);
                }
            }


    .. tab:: Kraken
        .. code-block:: java

            import com.ctre.phoenix6.configs.TalonFXConfiguration;
            import com.ctre.phoenix6.hardware.TalonFX;
            import com.ctre.phoenix6.signals.InvertedValue;
            import com.ctre.phoenix6.signals.NeutralModeValue;

            import edu.wpi.first.wpilibj2.command.SubsystemBase;
            import frc.robot.Constants.ChassisConstants;


            //File name must same with this
            //              ^
            //              |
            public class KrakenChassis extends SubsystemBase{
                public TalonFX LeftMotor, RightMotor;
                public TalonFXConfiguration LeftConfig, RightConfig;
                //Bruh, your hardware screams performance, but your code still whispers 'default template'.

                public KrakenChassis(){
                    LeftMotor = new TalonFX(ChassisConstants.LeftMotorID);
                    RightMotor = new TalonFX(ChassisConstants.RightMotorID);

                    LeftConfig = new TalonFXConfiguration();
                    RightConfig = new TalonFXConfiguration();

                    LeftConfig.MotorOutput
                        .withNeutralMode(NeutralModeValue.Brake)
                        .withInverted(InvertedValue.Clockwise_Positive);
                    
                    RightConfig.MotorOutput
                        .withNeutralMode(NeutralModeValue.Brake)
                        .withInverted(InvertedValue.CounterClockwise_Positive); //Anyway it must opposite with left side

                    LeftMotor.getConfigurator().apply(LeftConfig);
                    RightMotor.getConfigurator().apply(RightConfig);
                }

                public void drive(double speed, double rotation){
                    LeftMotor.set(speed+rotation);
                    RightMotor.set(speed-rotation);
                }
            }

.. note:: 
    Check out the references
    `DifferentialDrive <https://docs.wpilib.org/en/stable/docs/software/hardware-apis/motors/wpi-drive-classes.html#using-the-differentialdrive-class-to-control-differential-drive-robots>`_