import SocketServer
import threading
import nuke
import runpy
import os

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} sent:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        if os.path.exists(self.data): 
            runpy.run_path(self.data.strip())
        else:
            print "Path does not exist: %s"%self.data
        self.request.sendall(self.data.upper())

def begin():
    HOST, PORT = "localhost", 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Create the server, binding to localhost on port 9999
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name

    #server.shutdown()
    #server.server_close()
    
begin()

