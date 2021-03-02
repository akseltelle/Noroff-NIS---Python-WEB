import cgi

data = cgi.FieldStorage()
name = data.getvalue("name")
surname = data.getvalue("surname")
description = data.getvalue("description")


print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<head>")
print("<title>Student Details</title>")
print("</head>")
print("<body>")
print("<h1>{} {}</h1>".format(name, surname))
print("{}".format(description))
print("<br>")
print("<a href=\"capturestudent.html\">Back</a>")
print("</body>")
print("</html>")