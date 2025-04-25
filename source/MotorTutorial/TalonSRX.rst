TalonSRX Motor Controller Introduction
=======================================

TalonSRX motor controller is designed for brushed motor like CIM or mini-CIM which looks like

.. image:: https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/1/217-8080.jpg
   :alt: TalonSRX motor controller
   :width: 60%

Motor Definition
++++++++++++++++

.. code-block:: java

   public TalonSRX motor;
   //You can configure more settings by using the TalonSRXConfiguration class

   public something(){
      motor = new TalonSRX(0);

      motor.configAllSettings(new TalonSRXConfiguration());//restore settings

      motor.setInverted(InvertType.None); //set inverted, you can check out the InvertType class for more settings
      motor.setNeutralMode(NeutralMode.Brake);
   }

and you can drive the motor by this command 

.. code-block:: java

   public void drive(double speed){
        motor.set(TalonSRXControlMode.PercentOutput, speed); //you can checkout the TalonSRXControlMode to get the more information for driving motor methods.
   }