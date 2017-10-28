# PyCNC-with-WEB
PyCNC with Web interface

Install WebIOPi follow instructions http://webiopi.trouch.com/INSTALL.html

In htdocs folder you can find the web site installation.
The script.py is the python code that makes the interface with the web.
GPIO 25 has a Led connected to test web commands.

Note:
Append those paths with the correct folders inside the script.py so that
python can import code. Tricky to find.

sys.path.append('/home/pi/Desktop/PyCNC/PyCNC-master')
sys.path.append('/home/pi/Desktop/PyCNC/PyCNC-master/cnc/hal_raspberry')
