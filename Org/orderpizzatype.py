import cgi

data = cgi.FieldStorage()

price = 0
pizza_size = data.getvalue("size")
pizza_base = data.getvalue("base")

if pizza_base == "thin":
    if pizza_size == "small":
        price = 30
    if pizza_size == "medium":
        price = 50
    if pizza_size == "large":
        price = 70
if pizza_base == "thick":
    if pizza_size == "small":
        price = 34
    if pizza_size == "medium":
        price = 57
    if pizza_size == "large":
        price = 80

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Pizza Order</title>")
print("</head>")
print("<body>")
print("<h1>Pizza order:</h1>")
print("You ordered a {0} {1} base pizza at a price of {2:.2f}.<br/><br/>".format(pizza_size,pizza_base,price))
print("<a href=\"pizzatype.html\">Back</a>")
print("</body>")
print("</html>")