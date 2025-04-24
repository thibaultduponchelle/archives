# airsensor-linux-usb

The project was created on Sep 16, 2011.

Author : **JKN** (Rodric Yates ?)

Licence : [GNU Lesser GPL](http://www.gnu.org/licenses/lgpl.html)

From [google code archive page](https://code.google.com/archive/p/airsensor-linux-usb/)

## Summary

Provides a simple Qt/libusb-based program to read out the data of an AirSensor USB-stick

Simple program to display the air-quality measurements of an Air-Sensor USB-stick under Linux.

### About the device :

 + idVendor: 0x03eb Atmel Corp.
 + idProduct: 0x2013
 + iManufacturer: AppliedSensor
 + iProduct: iAQ Stick


### Libraries used:

 + Qt4
 + Qwt
 + libusb-0.1 (or: libusb-1.0 + libusb-compat)


## Original README

I was aiming for a quick-and-dirty solution to read out and display
the data of the Voltcraft CO-20 USB-stick.

I have NOT thoroughly analyzed the port-traffic under windows,
but simply took the part of the incoming byte-stream that seems
to yield reasonble results as compared to the windows-program.

Feel free to improve on it as I probably won't...

The Qt-part is based on the 'cpuplot'-example of QWT.

COMPILE:

 + qmake
 + make

HANDLING:

 + click the legend 'Air-Quality' to start/stop writing the data
   to a log-file ('./airsensor.log').

