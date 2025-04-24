TalonSRX Motor Controller Introduction
=======================================

The TalonSRX is a versatile motor controller from Cross the Road Electronics (CTRE) designed for FRC robotics applications. It's commonly used to control CIM motors, mini-CIMs, and other brushed DC motors in FRC competitions.

Features
--------

* PWM and CAN bus communication
* Closed-loop control capabilities
* Support for limit switches and encoders
* Programmable using the CTRE Phoenix Framework
* Current limiting and voltage compensation
* Multiple control modes: Position, Velocity, Current, MotionMagic

Setup and Configuration
----------------------

To use a TalonSRX in your robot code:

.. code-block:: java

   import com.ctre.phoenix.motorcontrol.can.WPI_TalonSRX;
   import com.ctre.phoenix.motorcontrol.ControlMode;
   
   // Create a TalonSRX with device ID 1
   WPI_TalonSRX motor = new WPI_TalonSRX(1);
   
   // Set the motor to run at 50% power
   motor.set(ControlMode.PercentOutput, 0.5);

Common Applications
------------------

* Drive train motors
* Arm mechanisms
* Elevator systems
* Intake mechanisms
