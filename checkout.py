# Import modules
import products as products                                             # Import products Module
import cgi                                                              # Import cgi Module

Ducati = products.Motorcycle.Ducati                                     # Define Ducati from Module "products"
Lamborghini = products.Car.Lamborghini                                  # Define Lamborghini from Module "products"
Ferrari = products.Car.Ferrari                                          # Define Ferrari from Module "products"

data = cgi.FieldStorage()                                               # Define data from from Module "cgi"

# Create values to be used
item1 = ""
item1_1 = ""
item2 = ""
item2_2 = ""
item3 = ""
item3_3 = ""
cars = ""
price = 0

if data.getvalue("Ducati"):                                            # Show product if selected
    if data.getvalue("Ducati") == "0":                                 # Show nothing if product amount is "0"
        cars += ""
    elif data.getvalue("Ducati") == "1":                               # View information for 1 x product
        item1 += "" + Ducati.id + ""                                   # Placeholder for checkout information
        item1_1 += "1"                                                 # Placeholder for checkout information
        cars += "" + data.getvalue(Ducati.id) + " x " + Ducati.name + ": ${:,.0f}".format(Ducati.price)
        cars += "<br>"
        cars += "<br>"
        price += Ducati.price
    elif data.getvalue("Ducati") == "2":                               # View information for 2 x product
        item1 += "" + Ducati.id + ""                                   # Placeholder for checkout information
        item1_1 += "2"                                                 # Placeholder for checkout information
        cars += "" + data.getvalue(Ducati.id) + " x " + Ducati.name + ": ${:,.0f}".format(Ducati.price)
        cars += "<br>"
        cars += "<br>"
        price += Ducati.price_2
    elif data.getvalue("Ducati") == "3":                               # View information for 3 x product
        item1 += "" + Ducati.id + ""                                   # Placeholder for checkout information
        item1_1 += "3"                                                 # Placeholder for checkout information
        cars += "" + data.getvalue(Ducati.id) + " x " + Ducati.name + ": ${:,.0f}".format(Ducati.price)
        cars += "<br>"
        cars += "<br>"
        price += Ducati.price_3
    else:                                                               # Show error if too many are added to cart
        item1 += "" + Ducati.id + ""                                    # Placeholder for checkout information
        cars += "Sorry, we do not have " + data.getvalue(Ducati.id) + " x " + Ducati.name + " in stock. Item not added to cart."
        cars += "<br>"
        cars += "<br>"
        price += 0.00

if data.getvalue("Lamborghini"):                                        # Show product if selected
    if data.getvalue("Lamborghini") == "0":                             # Show nothing if product amount is "0"
        cars += ""
    elif data.getvalue("Lamborghini") == "1":                           # View information for 1 x product
        item2 += "" + Lamborghini.id + ""                               # Placeholder for checkout information
        item2_2 += "1"                                                  # Placeholder for checkout information
        cars += "" + data.getvalue(Lamborghini.id) + " x " + Lamborghini.name + ": ${:,.0f}".format(Lamborghini.price)
        cars += "<br>"
        cars += "<br>"
        price += Lamborghini.price
    elif data.getvalue("Lamborghini") == "2":                           # View information for 2 x product
        item2 += "" + Lamborghini.id + ""                               # Placeholder for checkout information
        item2_2 += "2"                                                  # Placeholder for checkout information
        cars += "" + data.getvalue(Lamborghini.id) + " x " + Lamborghini.name + ": ${:,.0f}".format(Lamborghini.price)
        cars += "<br>"
        cars += "<br>"
        price += Lamborghini.price_2
    elif data.getvalue("Lamborghini") == "3":                           # View information for 3 x product
        item2 += "" + Lamborghini.id + ""                               # Placeholder for checkout information
        item2_2 += "3"                                                  # Placeholder for checkout information
        cars += "" + data.getvalue(Lamborghini.id) + " x " + Lamborghini.name + ": ${:,.0f}".format(Lamborghini.price)
        cars += "<br>"
        cars += "<br>"
        price += Lamborghini.price_3
    elif data.getvalue("Lamborghini") == "4":                           # View information for 4 x product
        item2 += "" + Lamborghini.id + ""                               # Placeholder for checkout information
        item2_2 += "4"                                                  # Placeholder for checkout information
        cars += "" + data.getvalue(Lamborghini.id) + " x " + Lamborghini.name + ": ${:,.0f}".format(Lamborghini.price)
        cars += "<br>"
        cars += "<br>"
        price += Lamborghini.price_4
    elif data.getvalue("Lamborghini") == "5":                            # View information for 5 x product
        item2 += "" + Lamborghini.id + ""                                # Placeholder for checkout information
        item2_2 += "5"                                                   # Placeholder for checkout information
        cars += "" + data.getvalue(Lamborghini.id) + " x " + Lamborghini.name + ": ${:,.0f}".format(Lamborghini.price)
        cars += "<br>"
        cars += "<br>"
        price += Lamborghini.price_5
    else:                                                               # Show error if too many are added to cart
        item2 += "" + Lamborghini.id + ""                               # Placeholder for checkout information
        cars += "Sorry, we do not have " + data.getvalue(Lamborghini.id) + " x " + Lamborghini.name + " in stock. Item not added to cart."
        cars += "<br>"
        cars += "<br>"
        price += 0.00

if data.getvalue("Ferrari"):                                            # Show product if selected
    if data.getvalue("Ferrari") == "0":                                 # Show nothing if product amount is "0"
        cars += ""
    elif data.getvalue("Ferrari") == "1":                               # View information for 1 x product
        item3 += "" + Ferrari.id + ""                                   # Placeholder for checkout information
        item3_3 += "1"                                                  # Placeholder for checkout information
        cars += "" + data.getvalue(Ferrari.id) + " x " + Ferrari.name + ": ${:,.0f}".format(Ferrari.price)
        cars += "<br>"
        cars += "<br>"
        price += Ferrari.price
    elif data.getvalue("Ferrari") == "2":                               # View information for 2 x product
        item3 += "" + Ferrari.id + ""                                   # Placeholder for checkout information
        item3_3 += "2"                                                  # Placeholder for checkout information
        cars += "" + data.getvalue(Ferrari.id) + " x " + Ferrari.name + ": ${:,.0f}".format(Ferrari.price)
        cars += "<br>"
        cars += "<br>"
        price += Ferrari.price_2
    else:                                                               # Show error if too many are added to cart
        item3 += "Ferrari"                                              # Placeholder for checkout information
        cars += "Sorry, we do not have " + data.getvalue(Ferrari.id) + " x " + Ferrari.name + " in stock. Item not added to cart."
        cars += "<br>"
        cars += "<br>"
        price += 0.00

cars += ""

print("Content-Type: text/html")
print()
print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head>")
print("<!-- META -->")
print("<meta charset='UTF-8'>")
print("<!-- TITLE -->")
print("<title>Kristaberslo | Checkout</title>")
print("</head>")
print("<body>")
print("<br>")
print("<h1>Checkout</h1>")
print("<hr>")
print("<a href='/'>Home</a>")
print("<hr>")
print(cars)                                                             # Print all products that have been selected by the customer
print("<h3>Checkout:</h3>")
print("<b>Total:</b> ${:,.0f}".format(price))
print("<br><br>")

# Add hidden information to "Pay Now" button to generate receipt.
if price == 0:
    print("<p>No items in cart</p>")
else:
    print("<form method='post' action='receipt.py'>")
    if item1 == "":
        print("")
    else:
        print("<input type='text' id='" + item1 + "' name='" + item1 + "' Value='" + item1_1 + "' hidden><br/>")
    if item2 == "":
        print("")
    else:
        print("<input type='text' id='" + item2 + "' name='" + item2 + "' Value='" + item2_2 + "' hidden><br/>")
    if item3 == "":
        print("")
    else:
        print("<input type='text' id='" + item3 + "' name='" + item3 + "' Value='" + item3_3 + "' hidden><br/>")
    print("")
    print("")
    print("<input type='submit' value='Pay Now' />")
    print("</form>")


print("<br>")
print("<a href='/'>Go back</a>")
print("<hr>")
print("<p>Copyright &copy; 2021 Kristaberslo AS.</p>")
print("</body>")
print("</html>")