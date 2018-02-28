from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from urlparse import urlparse




## CRUD OPERATIONS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catalog, CatalogItem

## CREATE SESSION AND CONNECTO TO DB
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith("/"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            entry = session.query(Catalog).all()
            message = ""
            message += "<html><body>"
            message += '<div><a href="/new">Add new catalog</a></div>'

            for i in entry:
                message += '<div>' + i.name + ' <a href="'+str(i.id)+'/edit">Edit</a><a href="'+str(i.id)+'/delete">Delete</a><div>'

            message += "</body></html>"
            self.wfile.write(message)
            print(message)
            return

        if self.path.endswith("/new"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>"
            message += '<div>Add new catalog</div>'
            message += '<form method="POST">Catalog Name:<br><input type="text" name="name"><br><input type="submit" value="Submit"></form>'
            message += "</body></html>"
            self.wfile.write(message)
            print(message)
            return

        else:
            self.send_error(404, 'File Not Found: %s' % self.path)


    def do_POST(self):
        # How long was the message?
        length = int(self.headers.get('Content-length', 0))

        # Read and parse the message
        data = self.rfile.read(length)

        # Not good since its hardcoded
        catalogname = data[5:]

        # Escape HTML tags in the message so users can't break world+dog.
        catalogname = catalogname.replace("<", "&lt;")

        # update database
        newCatalog = Catalog(name = catalogname)
        session.add(newCatalog)
        session.commit()

        # Send a 303 back to the root page
        self.send_response(303)  # redirect via GET
        self.send_header('Location', '/')
        self.end_headers()


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print("Web Server running on port %s") % port
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()
