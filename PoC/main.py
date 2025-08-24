# main.py
from wsgiref.simple_server import make_server
from wsgiref.validate import validator

from multipart.multipart import parse_options_header


def simple_app(environ, start_response):
    print(environ["CONTENT_TYPE"])
    _, _ = parse_options_header(environ["CONTENT_TYPE"])

    print("Done processing!")
    start_response("200 OK", [("Content-type", "text/plain")])
    return [b"Ok"]


httpd = make_server("", 8123, validator(simple_app))
print("Serving on port 8123...")
httpd.serve_forever()
