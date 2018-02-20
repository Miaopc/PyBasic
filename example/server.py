import http.server, os
os.chdir("/home/pi/Linux")
httpd = http.server.HTTPServer(('192.168.31.138', 5000),
		http.server.SimpleHTTPRequestHandler)
httpd.serve_forever()
