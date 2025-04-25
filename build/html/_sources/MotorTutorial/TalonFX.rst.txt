TalonFX Motor Controller Introduction
======================================

TalonFX is the Motor Contoller used by Kraken Series, it is intergrated in the motor so there's no specific image for it.

.. attention:: 
   VendorDeps: Phoenix6

Motor Definition
++++++++++++++++

.. code-block:: java

   public TalonFX motor;
   public TalonFXConfiguration config;

   public void KrakenMotorConfig(){
        motor = new TalonFX(0);
        config = new TalonFXConfiguration();

        //Current Limitations to 80 Amps
        config.CurrentLimits
            .withStatorCurrentLimit(80)
            .withStatorCurrentLimitEnable(true);

        //configure inverted and neural mode (IdleMode for SparkMax)
        config.MotorOutput
            .withInverted(InvertedValue.Clockwise_Positive)
            .withNeutralMode(NeutralModeValue.Brake);
    }

and you can drive the motor by using these two method

.. code-block:: java

   public void normalDrive(dobule speed){
      motor.set(speed);
   }

   //or

   pubic DutyCycleOut driving = new DutyCycleOut(0.0);
   pubic void DutyCycleDrive(double speed){
      motor.setControl(driving.withOutput(speed))
   }