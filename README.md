# FreeDIY-EE-VPN
This project works by taking an android device and connecting it to your computer though a USB cable and running the connection through 4G. 
EE was used in this project but any 4G service provider can be used as long as they change the provided IP address to your phone every time flight  mode is switched on. 
EE was used here as it is a large UK based 4G provider and has hundreds of thousands of IP addresses.

This program is a really basic proof of concept that uses a samsung galaxy s5 in developers mode and connects to it using (https://androidmtk.com/download-minimal-adb-and-fastboot-tool)
. A samsung s5 was used as it has the ability to mobile hotspot through USB cable. Secondly, remember when using the python adb library the adb shell must be running on the host machine before the library can work

If you want to read more about what is possible with Android Adb see this helpful article here (https://itnext.io/how-you-can-control-your-android-device-with-python-45c3ab15e260)

This project works fine and the internal methods can be called from other python functions to switch the ip address of the host machine. One thing to note is that I have noticed that it can make certain applications throw non-blocking OS errors (if running on windows). IP address switching just seems to be something that windows doesn't like natively if you do it through a mobile hotspot.
