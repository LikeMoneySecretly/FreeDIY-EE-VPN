# FreeDIY-EE-VPN
This project works by taking an android device and connecting it to your computer though a USB cable and running the connection through 4G, EE was used in this project but any 4G service provider
can be used as long as they change the provided IP address to your phone every time flight mode is switched on. 
EE was used here as it is a large UK based 4G provider and has hundreds of thousands of IP addresses.

This program is a really basic proof of concept that uses a samsung galaxy s5 in developers mode and connects to it using (https://androidmtk.com/download-minimal-adb-and-fastboot-tool)
. Remember, when using the python adb library the adb shell must be running on the host machine 

If you want to read more about what is possible with Android Adb see this helpful article here (https://itnext.io/how-you-can-control-your-android-device-with-python-45c3ab15e260)
