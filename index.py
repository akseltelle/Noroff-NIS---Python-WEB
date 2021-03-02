# Import modules
import products as products                                             # Import products Module

Ducati = products.Motorcycle.Ducati                                     # Define Ducati from Module "products"
Lamborghini = products.Car.Lamborghini                                  # Define Lamborghini from Module "products"
Ferrari = products.Car.Ferrari                                          # Define Ferrari from Module "products"

print("Content-Type: text/html")                                        # Set content type to TEXT/HTML
print()
print("<!DOCTYPE html>")                                                # Set doctype to HTML
print("<html lang='en'>")                                               # Set language to English

# Head Start
print("<head>")
print("<!-- META -->")
print("<meta charset='UTF-8'>")
print("<!-- TITLE -->")
print("<title>Kristaberslo | Home</title>")
print("</head>")

# Body Start
print("<body>")
print("<br>")
print("<h1>Welcome to Kristaberslo</h1>")
print("<hr>")
print("<a href='/'>Home</a>")
print("<hr>")
print("<form method='post' action='checkout.py'>")
print("<h2>Items for sale</h2>")
print("<br>")

# First Product
print("<h3>" + Ducati.name + "</h3>")
print("<p><a href='/info.py?id=" + Ducati.id + "'>More info</a></p>")
print("<p><b>Category:</b> " + Ducati.category + "</p>")
print("<p><b>Price:</b> ${:,.0f}</p>".format(Ducati.price))
print("<p><b>Available:</b> " + Ducati.available + " </p><br>")
print("<label for='" + Ducati.id + "'>Amount:</label>")
print("<input type='number' id='" + Ducati.id + "' name='" + Ducati.id + "' min='0' max='" + Ducati.available + "'><br>")
print("<br>")
print("<br>")

# Second Product
print("<h3>" + Lamborghini.name + "</h3>")
print("<p><a href='/info.py?id=" + Lamborghini.id + "'>More info</a></p>")
print("<p><b>Category:</b> " + Lamborghini.category + "</p>")
print("<p><b>Price:</b> ${:,.0f}</p>".format(Lamborghini.price))
print("<p><b>Available:</b> " + Lamborghini.available + " </p><br>")
print("<label for='" + Lamborghini.id + "'>Amount:</label>")
print("<input type='number' id='" + Lamborghini.id + "' name='" + Lamborghini.id + "' min='0' max='" + Lamborghini.available + "'><br/>")
print("<br>")
print("<br>")

# Third Product
print("<h3>" + Ferrari.name + "</h3>")
print("<p><a href='/info.py?id=" + Ferrari.id + "'>More info</a></p>")
print("<p><b>Category:</b> " + Ferrari.category + "</p>")
print("<p><b>Price:</b> ${:,.0f}</p>".format(Ferrari.price))
print("<p><b>Available:</b> " + Ferrari.available + " </p><br>")
print("<label for='" + Ferrari.id + "'>Amount:</label>")
print("<input type='number' id='" + Ferrari.id + "' name='" + Ferrari.id + "' min='0' max='" + Ferrari.available + "'><br/>")
print("<br>")
print("<br>")

# Submit and footer
print("<input type='submit' value='Place Order' />")
print("</form>")
print("<hr>")
print("<p>Copyright &copy; 2021 Kristaberslo AS.</p>")
print("</body>")
print("</html>")
