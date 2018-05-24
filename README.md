A simple application to make a scanner remotely available, typically to be used with a raspberry pi.

## Background 
If you want a wireless printer and scanner, you can buy one for, say $100. Or get a cheap all in one for $20 or so and a raspberry pi (or pi zero) and make it a wireless printer. 
Long term objective is also to make the printer a air-print compatible one so that you can print from a iOS device.

## Printing and Scanning
For the most part, all mainstream vendor's printers (and all-in-ones) have a decent driver for Raspibian. Installing the printer driver would take care of exposing the printer over the network.

Remote scanning is generally not that widely supported.

There are multiple options for printing. 

## CUPS
--Add details--

## HP Printers
The HP Linux drivers can be got from [HP Linux Imaging and Printing](https://developers.hp.com/hp-linux-imaging-and-printing) page. There is an automatic installerr on the website, but a couple of dependencies need to be compiled/built. If you want to go the hplip route for printing, follow these steps:
Install sip:
- Download sources from https://www.riverbankcomputing.com/software/sip/download

  ```
  wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.8/sip-4.19.8.tar.gz
  ```
- Untar the file

Install qt5:

wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.8/sip-4.19.8.tar.gz
tar -zxvf sip-4.19.8.tar.gz
cd sip-4.19.8/
make
sudo make install
cd ..
cd PyQt5_gpl-5.10.1/
python configure.py



wget https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.10.1/PyQt5_gpl-5.10.1.tar.gz
tar -zxvf PyQt5_gpl-5.10.1.tar.gz
cd PyQt5_gpl-5.10.1
python configure.py



sudo su
apt-get update
apt-get install hplip cups
usermod -a -G lpadmin pi

## Sane
[Sane](http://sane-project.org) is almost always the best way to access a scanner over command line on Linux.

## The project

### Pre-Requisities

- A Linux machine. Something portable like the raspberry pi so that you can attach it to the wired printer/scanner amd make it wireless. There is nothing in the code that is pi specific.

- Python 2.x. I have plans to provide a python 3 version, but till then 2.x

- Sane (from http://sane-project.org)

### What it does
- scan.sh has calls to scanimage with various parameters. 
- simpleServerWith