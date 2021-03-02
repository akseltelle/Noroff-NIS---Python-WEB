# Import modules
import products as products                                             # Import products Module
import cgi                                                              # Import cgi Module

Ducati = products.Motorcycle.Ducati                                     # Define Ducati from Module "products"
Lamborghini = products.Car.Lamborghini                                  # Define Lamborghini from Module "products"
Ferrari = products.Car.Ferrari                                          # Define Ferrari from Module "products"
Null = products.Error.Null                                              # Define Error message from Module "products"

data = cgi.FieldStorage()                                               # Define data from from Module "cgi"

if data.getvalue("id") == "Ducati":
    product = Ducati
elif data.getvalue("id") == "Lamborghini":
    product = Lamborghini
elif data.getvalue("id") == "Ferrari":
    product = Ferrari
else:
    product = Null

print("Content-Type: text/html")
print()
print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head>")
print("<!-- META -->")
print("<meta charset='UTF-8'>")
print("<!-- TITLE -->")
print("<title>Kristaberslo | " + product.name + "</title>")
print("</head>")
print("<body>")
print("<br>")
print("<h1>About " + product.name + "</h1>")
print("<hr>")
print("<a href='/'>Home</a>")
print("<hr>")
print("<img src='" + product.image + "' class='rounded' width='500px'>")
print("<h2>" + product.name + "</h2>")
print("<p><b>Price:</b> ${:,.0f}</p>".format(product.price))
print("<p><b>Category:</b> " + product.category + "</p>")
print("<p><b>Description:</b> " + product.description + "</p>")
print("<br><br><br>")
print("<a href='/'>Go Back</a>")
print("<hr>")
print("<p>Copyright &copy; 2021 Kristaberslo AS.</p>")
print("</body>")
print("</html>")
