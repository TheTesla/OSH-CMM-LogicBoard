# Coordinate Measurement Arm Logic Board

This logic board implements the main functionality of the 5-dof coordinate measurement arm. The central component is an _Arduino UNO R3_. It reads the rotary encoders out and provides the communication to the host PC and power supply via the USB port. 

The 5 rotary encoders are plugged into the D-Sub-9 socket. The board implements electrical protection circuits, that the _Arduino_ won't be damaged, if voltage is accidentally applied to the encoder connectors. Unfortunatelly, the  USB port can't be protected, because it is directly part of the _Aduino_.

The board also boosts the power supply voltage from the USB port to operate the rotary encoders.

## Implementation

The rotary encoders are powered by a 5 V to 9 V voltage converter, because they need at least 5 V. This lower limit is not maintained by the USB port, which can deliver down to 4.75 V.

Diodes protect the board from excessive positive voltage from the encoder connectors, while a 3 transistors protect it from short circuit and negative voltage levels on the encoder supply line.

The encoder data lines are connected via 10k resistors to the _Arduino_ to protect the inputs against excessive voltage from the encoder connector.

The open collector outputs of the encoders need pull-up resistors. These are integrated into the plug of the encoder itself.


