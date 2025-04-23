Swerve Chassis Tutorial
=======================


The swerve chassis is one of the most advanced drivetrains in FRC, offering exceptional speed, power, and maneuverability, which is why it’s commonly used by top-tier teams. However, it requires the most tuning and debugging to achieve optimal performance.

Swerve chassis image below:

.. image:: https://www.chiefdelphi.com/uploads/default/98c9352ca78c34dfdc08f8b46b30b17e24915dd6
    :alt: Swerve Chassis Image

+++++++++++++++++++++++++
Swerve Chassis Dependices
+++++++++++++++++++++++++

| 8 motors (4 wheels, 2 motors per module)
| 4 encoders (1 per module, usually use CANCoder)
| 1 gyro (1 per robot)

.. note:: 
    If you use all CTRE products (kraken motor, cancoder, pigeon), you can unlock hidden feature called Swerve Project Generator in Phoenix Tuner X 

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

.. note:: 
    The CANCoder is not always percise for our robot, so we need to calibrate the CANCoder by :ref:`CANCoder-Calibration`
    

.. _CANCoder-Calibration:

CANCoder Calibration
++++++++++++++++++++

hello