import SimpleHTTPServer
import urlparse
import cgi
import subprocess

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):


    def do_POST(self):
        parsedParameters = urlparse.urlparse(self.path)
        queryParsed = urlparse.parse_qs(parsedParameters.query)
        self.processOperation(queryParsed);

    def do_GET(self):
        parsedParameters = urlparse.urlparse(self.path)
        queryParsed = urlparse.parse_qs(parsedParameters.query)
        print "[doGet]Query Parameters:", queryParsed
        if len(queryParsed) == 0:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self);
        else:
            self.processOperation(queryParsed)
    
    def processOperation(self, query):
        
        #Set Defaults
        folder = "scans" 
        fileName = folder + "/" + "scan"
        operation = "scan"
        scanMode = "color"
        resolution = 100
        pageDims = False
        l = -1
        t = -1
        width = -1
        height = -1
        format = "pdf"
        preview = False;
        unit = "mm"
        
        #Get values from parameters
        if ('fileName' in query ):
            fileName = folder + "/" + query['fileName'][0]
        if ('format' in query ):
            format = query['format'][0]
        if ('operation' in query ):
            operation = query['operation'][0]
        if ('scanMode' in query ):
            scanMode = query['scanMode'][0]
        if('resolution' in query):
            resolution = query['resolution'][0]
        if('l' in query):
            l = query['l'][0]
        if('t' in query):
            t = query['t'][0]
        if('width' in query):
            width = query['width'][0]
        if('height' in query):
            height = query['height'][0]
        if('preview' in query):
            preview = True;

        if(l < 0 or t < 0 or width < 0 or height < 0):
            print "[processOperation] At least one Page Dim not present, taking default"
            pageDims = False;
        else:
            pageDims = True
            FACTOR = 3.93;
            l = int(l) / FACTOR
            t = int(t) / FACTOR
            width = int(width) / FACTOR
            height = int(height) / FACTOR
        
        if preview:
            format = 'jpg'
            resolution = 100
            print '[processOperation] Preview mode, defaulting format to jpg and resolution to 100'
            
        print "[processOperation] Params: fileName: {}, format: {}, operation: {}, scanMode: {}, resolution: {}, left: {}, top: {}, width: {}, height: {}, preview: {}, unit: {}".format(fileName, format, operation, scanMode, resolution, l, t, width, height, preview, unit)
        
        if operation == "scan":
            if(l < 0 or t < 0 or width < 0 or height < 0):
                try:
                    out = subprocess.check_output(["sh", "scan.sh", fileName, format, scanMode, str(resolution), unit])
                    print "[processOperation] output from scan:", out
                    self.sendSuccessResponse(fileName + "." + format)
                except CalledProcessError:
                    print "[processOperation] Error scanning.", sys.exc_info()[0]
                    self.sendErrorResponse("[processOperation] Error while trying to preview/scan. Check if the scanner is connected and powered up");
            else:
                try:
                    print "[processOperation] Calling shell,", "scan.sh", fileName, format, scanMode, str(resolution), unit, str(l), str(t), str(width), str(height)
                    out = subprocess.check_output(["sh", "scan.sh", fileName, format, scanMode, str(resolution), unit, str(l), str(t), str(width), str(height)])
                    self.sendSuccessResponse(fileName + "." + format)
                except CalledProcessError:
                    print "[processOperation] Error scanning.", sys.exc_info()[0]
                    self.sendErrorResponse("[processOperation] Error while trying to preview/scan. Check if the scanner is connected and powered up");
            
            print "[processOperation] scanned, output from shell: ", out
            
        else:
            self.send_response(500)
            self.send_header('Content-Type', 'text/html') #application/pdf
            self.end_headers()
            self.wfile.write("[processOperation] Unknown Operaton "+ operation)
            
        self.wfile.close();
        
    def sendSuccessResponse(self, fileName):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(fileName);
    
    def sendErrorResponse(self, errorMessage):
        self.send_response(500)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(errorMessage);
