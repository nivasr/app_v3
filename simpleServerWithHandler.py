import SocketServer
import MyHandler

PORT = 8000

#Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler = MyHandler.MyHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at portt", PORT
httpd.serve_forever()
