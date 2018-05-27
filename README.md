A simple application to make a scanner remotely available, typically to be used with a raspberry pi.


### Pre-Requisities
- A Linux machine. Something portable like the raspberry pi so that you can attach it to the wired printer/scanner amd make it wireless. There is nothing in the code that is pi specific.
- Python 2.x. I have plans to provide a python 3 version, but till then 2.x
- Sane (from http://sane-project.org) and Sane compatible scanner driver. Typiucally from the scanner/all in one vendor.

### How to run
- Run `startScannerApp.sh`
- Access ip:8000 from a browser. Eg., http://localhost:8000 to access from the local (raspberry pi) browser

### Features
- Preview and Scan
- Change dimensions/crop
- Custom name
- Multiple formats: pdf, jpg, png, tiff. The scan itself is in tiff and is converted to one of these formats.
- Multiple resolutions: 75, 100, 200, 300, 600, 1200, 2400. Resolutions are dependent on the scanner. 

### Future
- Allow paper size selections
- Better paper dimension handling
- A bot more beautification

### What it does
- `scan.sh` has calls to `scanimage` with various parameters. [`scanImage`](http://www.sane-project.org/man/scanimage.1.html) is the [sane](http://www.sane-project.org/man/sane.7.html) command line interface
- `simpleServerWithHandler.py`: A simple python http server
- `index.html` - a simple UI for the scan