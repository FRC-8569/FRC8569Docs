SparkMax Motor Controller Introduction
=======================================

.. image:: https://cdn11.bigcommerce.com/s-t3eo8vwp22/images/stencil/960w/products/360/2795/MAX_HERO-noflag__60247.1692730069.png
    :alt: SparkMax
    :width: 60%

SparkMax motor controller is produced by REVRobotics, it can use on both brushed and brushless motors.

**Software API: REVLib**


Motor Definition
++++++++++++++++

.. note:: 
    Every configuration is not required, you can config all the settings you need


.. tabs::
    .. tab:: NEO
        .. code-block:: java
            
            public SparkMax motor; //Motor itself
            public SparkMaxConfig config; //motor config
            public RelativeEncoder encoder; //built in encoder

            pubic void configMotor(){
                motor = new SparkMax(0, MotorType.kBrushless);//you can configure the motor type bewteen kBrushless and kBrushed
                config = new SparkMaxConfig();

                config
                    .idleMode(IdleMode.kBrake) //The motor mode, kBrake will stop motor immediately otherwise will spin untill stop naturally
                    .inverted(false) //configure if the motor inverted
                    .follow(0); //you can set the motor followed to another motor, usually used in 4 motor KOP chassis

                motor.configure(config, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters); //apply settings to the motor
            }

.. _BrakevsCoast:

The Differences between kBrake and kCoast
+++++++++++++++++++++++++++++++++++++++++

.. list-table:: 
    :width: 100%
    :widths: 34 33 33
    :header-rows: 1
    
    * - 
  
      - kBrake
  
      - kCoast

    * - Behaviours
  
      - stop instantly
  
      - spin untill stop naturally
  
    * - code
      
      - IdleMode.kBrake
  
      - IdleMode.kCoast
  
    * - common usage

      - Most of the time

      - CANCoder Calibrating
.. note::
    check out the references:
    `Closedloop Contol <https://docs.revrobotics.com/brushless/revlib/closed-loop-control-overview/closed-loop-control-getting-started>`_
    `Configuring SparkMax <https://docs.revrobotics.com/revlib/spark/configuring-a-spark>`_