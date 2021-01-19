import cgi, os, random, string

data = cgi.FieldStorage()

upload = data["imagefile"]

filename = os.path.basename(upload.filename)


with open(filename, "wb") as copy:
    copy.write(upload.file.read())


print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Image Upload</title>")
print("</head>")
print("<body>")
print("<h1>{}</h1>".format(filename))
print("<img src=\"{}\" width=\"100%\"><br/><br/>".format(filename))
print("<a href=\"imageupload.html\">Back</a>")
print("</body>")
print("</html>")

get_random_string(8)
