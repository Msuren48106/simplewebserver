from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>Top Software Companies</title>
</head>
<body align="center">
<caption>Top 5 software companies</caption>
<table>
<table border="1" cellspacing="2" cellpadding="2" align="center">
            <tr>
                <th>Rank</th>
                <th>Company Name</th>
                <th>Revenue(billion dollars)</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Block inc.(SQ).</td>
                <td>16.96</td>
            </tr>
            <tr>
                <td>2</td>
                <td>intuit inc.</td>
                <td>13.32</td>
            </tr>
            <tr>
                <td>3</td>
                <td>VMware inc.</td>
                <td>13.17</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Adyen NV</td>
                <td>8.14</td>
            </tr>           <tr>
                <td>5</td>
                <td>ServiceNow inc.</td>
                <td>6.92</td>
</table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()