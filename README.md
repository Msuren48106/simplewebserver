# EX01 Developing a Simple Webserver
## Date: 26.2.2024

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
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
```


## OUTPUT:
![alt text](<Screenshot (1).png>)
![alt text](<Screenshot (2).png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
