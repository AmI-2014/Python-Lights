# REST operation of Lights in Python #

The modules provided in this repository show how lights can be operated (i.e., turned on or off) on Hue and Z-Wave networks using REST.

* The ''rest.py'' module provides a really basic API for easily calling REST services.
* The ''hue.py'' shows how to turn on every light connected to a Hue bridge and to set the color loop effect on them: the lamps cycle through all the available hues for 10s, then they are all turned off.
* The ''zway.py'' shows how to turn on every "switch" device (i.e., lamps) connected to the Z-Wave network. Lamps are turned on and, after 10s, they are turned off. *Please be aware that this module only works on machines running the [ZWay server](http://razberry.z-wave.me), i.e., RaspberryPi+RaZBerry*