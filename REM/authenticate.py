import cgi

data = cgi.FieldStorage()
username = data.getvalue("username")
password = data.getvalue("password")

error = "Username or password wrong"
description = "Username or password wrong"

if username == "admin":
    if password == "password":
        url = "<a href='manager.py?id=jhu8lH79Gf'>Login success! Click to continue</a>"
        description = "Login success"
    else:
        description = "Username or password wrong"
else:
        description = "Username or password wrong"

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<head>")
print("<title>Kristaberslo | Authenticating</title>")
print("</head>")
print("<body>")
print("{}".format(url))
print("<br>")
print("Result: {}".format(description))
print("</body>")
print("</html>")