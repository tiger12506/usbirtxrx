# USB UART -> IR TX/RX

This code provides a working proof-of-concept for a USB serial-controlled IR transmit and receive device.
It is meant to use ridiculously cheap hardware from China to get computer controlled IR tx/rx in a more light-weight
fashion than you would see from lircd.

## Hardware needed:
[AliExpress 5V IR Infrared Decoder Encoding Transmitter Receiver...](https://www.aliexpress.us/item/3256802829723720.html)
[AliExpress CP2102 Type-C MICRO USB to UART TTL...](https://www.aliexpress.us/item/3256807364936421.html)

## Connections:
UART module -> IR module
5V -> 5V
Gnd -> Gnd
TX -> RX
RX -> TX

## Special sauce:
The IR encode/decode chip handles most of the work.
Simple remotes so far seem to follow a pattern of 2-byte manufacturer code, 1-byte action code, and upon receiving an IR code,
those three bytes get transmitted throught the UART to serial device (ex: /dev/ttyUSB0)

Transmit is handled by sending the prefix b'\xA1\xF1' in front of the 3-byte remote code. The prefix tells the ir chip to send
the following remote code.

## Caveats:
Almost certainly this does not handle repeating codes. (ex: volume up/down)

