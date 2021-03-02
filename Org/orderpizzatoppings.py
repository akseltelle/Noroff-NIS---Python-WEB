import cgi

data = cgi.FieldStorage()


toppings = "<ul>"
price = 0

if data.getvalue("cheese"):
    toppings += "<li>" + data.getvalue("cheese") + ": $0.50</li>"
    price += 0.50

if data.getvalue("bacon"):
    toppings += "<li>" + data.getvalue("bacon") + ": $0.90</li>"
    price += 0.90

if data.getvalue("pineapple"):
    toppings += "<li>" + data.getvalue("pineapple") + ": $0.70</li>"
    price += 0.70

if data.getvalue("avocado"):
    toppings += "<li>" + data.getvalue("avocado") + ": $0.80</li>"
    price += 0.80

if data.getvalue("tips"):
    toppings += "<li>" + data.getvalue("tips") + ": $1.00</li>"
    price += 1.00

toppings += "</ul>"

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Pizza Order</title>")
print("</head>")
print("<body>")
print("<h1>List of toppings:</h1>")
print(toppings)
print("Price: ${0:.2f}<br><br>".format(price))
print("<a href=\"pizzatoppings.html\">Back</a>")
print("</body>")
print("</html>")