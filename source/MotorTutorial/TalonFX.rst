TalonFX Motor Controller Introduction
======================================

The TalonFX is an integrated motor controller built into the Falcon 500 brushless motor, manufactured by VEX Robotics in collaboration with Cross the Road Electronics (CTRE). This combination provides a powerful and compact solution for FRC robotics teams.

Features
--------

* Integrated motor controller and brushless motor
* High power-to-weight ratio
* Built-in encoder for precise position and velocity feedback
* CAN bus communication
* Advanced closed-loop control algorithms
* Current limiting and voltage compensation
* Multiple control modes: Position, Velocity, Current, MotionMagic

Technical Specifications
-----------------------

* Maximum power: 500W
* Free speed: 6,380 RPM
* Stall torque: 4.69 N·m (3.46 ft·lbs)
* Integrated sensor resolution: 2,048 CPR

Example Code
-----------

Here's a basic example of how to use a TalonFX in Java:

.. code-block:: java

   import com.ctre.phoenix.motorcontrol.can.WPI_TalonFX;
   import com.ctre.phoenix.motorcontrol.ControlMode;
   
   // Create a TalonFX with device ID 1
   WPI_TalonFX motor = new WPI_TalonFX(1);
   
   // Configure factory defaults
   motor.configFactoryDefault();
   
   // Set the motor to run at 50% power
   motor.set(ControlMode.PercentOutput, 0.5);

Common Applications
------------------

* High-performance drive trains
* Shooters and launchers
* Climbing mechanisms
* Any application requiring high power and precise control
