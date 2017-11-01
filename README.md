# PyCNC-Web
PyCNC with Web interface
Original version by Nikolay-Kha/PyCNC

This cloned version is being transformed to support web interface to control a multiaxis CNC machine.
In order to be used as a Laser Cutter/Engraver the code will support a new axis to control a Laser diode.

Required:
  Install WebIOPi follow instructions http://webiopi.trouch.com/INSTALL.html

Configure the WebIOPi server /etc/webiopi/config, correct the folder to where you have installed PyCNC Web
  myscript = /home/pi/Desktop/PyCNC/PyCNC-master/cnc/script.py  
  doc-root = /home/pi/Desktop/PyCNC/PyCNC-master/htdocs     

In the /PyCNC-master/htdocs folder you will find the web site files accessible in the browser address:
  http://raspberrypi:8000/

The script.py is the python code that makes the interface with the web.
GPIO 25 has a Led connected to test web commands.

Note:
  Append those paths with the correct folders inside the script.py so that
  python can import code. This one was tricky to find.

  sys.path.append('/home/pi/Desktop/PyCNC/PyCNC-master')<br>
  sys.path.append('/home/pi/Desktop/PyCNC/PyCNC-master/cnc/hal_raspberry')


<img src="https://github.com/eirasys/PyCNC-with-WEB/blob/master/PyCNC%20with%20Web%20Interface.png?raw=true">
