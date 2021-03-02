# Import modules
import products as products                                             # Import products Module
import cgi                                                              # Import cgi Module
from datetime import *                                                  # Import datetime Module

Ducati = products.Motorcycle.Ducati                                     # Define Ducati from Module "products"
Lamborghini = products.Car.Lamborghini                                  # Define Lamborghini from Module "products"
Ferrari = products.Car.Ferrari                                          # Define Ferrari from Module "products"

data = cgi.FieldStorage()                                               # Define data from from Module "cgi"

receiptdate = datetime.today()                                          # Define now from from Module "datetime"


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
        item1 += "" + Ducati.id + ""                                   # Placeholder for receipt information
        item1_1 += "1"                                                 # Placeholder for receipt information
        cars += "<tr>"
        cars += "<th>" + item1_1 + "</th>"
        cars += "<th>" + Ducati.name + "</th>"
        cars += "<th>${:,.0f}</th>".format(Ducati.price)
        cars += "</tr>"
        price += Ducati.price
    elif data.getvalue("Ducati") == "2":                               # View information for 2 x product
        item1 += "" + Ducati.id + ""                                   # Placeholder for receipt information
        item1_1 += "2"                                                 # Placeholder for receipt information
        cars += "<tr>"
        cars += "<th>" + item1_1 + "</th>"
        cars += "<th>" + Ducati.name + "</th>"
        cars += "<th>${:,.0f}</th>".format(Ducati.price)
        cars += "</tr>"
        price += Ducati.price_2
    elif data.getvalue("Ducati") == "3":                               # View information for 3 x product
        item1 += "" + Ducati.id + ""                                   # Placeholder for receipt information
        item1_1 += "3"                                                 # Placeholder for receipt information
        cars += "<tr>"
        cars += "<th>" + item1_1 + "</th>"
        cars += "<th>" + Ducati.name + "</th>"
        cars += "<th>${:,.0f}</th>".format(Ducati.price)
        cars += "</tr>"
        price += Ducati.price_3
    else:                                                               # Show error if too many are added to cart
        item1 += "" + Ducati.id + ""                                    # Placeholder for receipt information
        cars += "<tr>"
        cars += "<th>0</th>"
        cars += "<th>" + Ducati.name + "</th>"
        cars += "<th>Sorry, we do not have " + data.getvalue(Ducati.id) + " x " + Ducati.name + " in stock. Item not added to cart.</th>"
        cars += "</tr>"
        price += 0.00

if data.getvalue("Lamborghini"):                                        # Show product if selected
    if data.getvalue("Lamborghini") == "0":                             # Show nothing if product amount is "0"
        cars += ""
    elif data.getvalue("Lamborghini") == "1":                           # View information for 1 x product
        item2 += "" + Lamborghini.id + ""                               # Placeholder for receipt information
        item2_2 += "1"                                                  # Placeholder for receipt information
        cars += "<tr>"
        cars += "<th>" + item2_2 + "</th>"
        cars += "<th>" + Lamborghini.name + "</th>"
        cars += "<th>${:,.0f}</th>".format(Lamborghini.price)
        cars += "</tr>"
        price += Lamborghini.price
    elif data.getvalue("Lamborghini") == "2":                           # View information for 2 x product
        item2 += "" + Lamborghini.id + ""                               # Placeholder for receipt information
        item2_2 += "2"                                                  # Placeholder for receipt information
        cars += "<tr>"
        cars += "<th>" + item2_2 + "</th>"
        cars += "<th>" + Lamborghini.name + "</th>"
        cars += "<th>${:,.0f}</th>".format(Lamborghini.price)
        cars += "</tr>"
        price += Lamborghini.price_2
    elif data.getvalue("Lamborghini") == "3":                           # View information for 3 x product
        item2 += "" + Lamborghini.id + ""                               # Placeholder for receipt information
        item2_2 += "3"                                                  # Placeholder for receipt information
        cars += "<tr>"
        cars += "<th>" + item2_2 + "</th>"
        cars += "<th>" + Lamborghini.name + "</th>"
        cars += "<th>${:,.0f}</th>".format(Lamborghini.price)
        cars += "</tr>"
        price += Lamborghini.price_3
    elif data.getvalue("Lamborghini") == "4":                           # View information for 4 x product
        item2 += "" + Lamborghini.id + ""                               # Placeholder for receipt information
        item2_2 += "4"                                                  # Placeholder for receipt information
        cars += "<tr>"
        cars += "<th>" + item2_2 + "</th>"
        cars += "<th>" + Lamborghini.name + "</th>"
        cars += "<th>${:,.0f}</th>".format(Lamborghini.price)
        cars += "</tr>"
        price += Lamborghini.price_4
    elif data.getvalue("Lamborghini") == "5":                           # View information for 5 x product
        item2 += "" + Lamborghini.id + ""                               # Placeholder for receipt information
        item2_2 += "5"                                                  # Placeholder for receipt information
        cars += "<tr>"
        cars += "<th>" + item2_2 + "</th>"
        cars += "<th>" + Lamborghini.name + "</th>"
        cars += "<th>${:,.0f}</th>".format(Lamborghini.price)
        cars += "</tr>"
        price += Lamborghini.price_5
    else:                                                               # Show error if too many are added to cart
        item2 += "" + Lamborghini.id + ""                               # Placeholder for receipt information
        cars += "<tr>"
        cars += "<th>0</th>"
        cars += "<th>" + Lamborghini.name + "</th>"
        cars += "<th>Sorry, we do not have " + data.getvalue(Lamborghini.id) + " x " + Lamborghini.name + " in stock. Item not added to cart.</th>"
        cars += "</tr>"
        price += 0.00

if data.getvalue("Ferrari"):                                            # Show product if selected
    if data.getvalue("Ferrari") == "0":                                 # Show nothing if product amount is "0"
        cars += ""
    elif data.getvalue("Ferrari") == "1":                               # View information for 1 x product
        item3 += "" + Ferrari.id + ""                                   # Placeholder for receipt information
        item3_3 += "1"                                                  # Placeholder for receipt information
        cars += "<tr>"
        cars += "<th>" + item3_3 + "</th>"
        cars += "<th>" + Ferrari.name + "</th>"
        cars += "<th>${:,.0f}</th>".format(Ferrari.price)
        cars += "</tr>"
        price += Ferrari.price
    elif data.getvalue("Ferrari") == "2":                               # View information for 2 x product
        item3 += "" + Ferrari.id + ""                                   # Placeholder for receipt information
        item3_3 += "2"                                                  # Placeholder for receipt information
        cars += "<tr>"
        cars += "<th>" + item3_3 + "</th>"
        cars += "<th>" + Ferrari.name + "</th>"
        cars += "<th>${:,.0f}</th>".format(Ferrari.price)
        cars += "</tr>"
        price += Ferrari.price_2
    else:                                                               # Show error if too many are added to cart
        item3 += "" + Ferrari.id + ""                                   # Placeholder for receipt information
        cars += "<tr>"
        cars += "<th>0</th>"
        cars += "<th>" + Ferrari.name + "</th>"
        cars += "<th>Sorry, we do not have " + data.getvalue(Ferrari.id) + " x " + Ferrari.name + " in stock. Item not added to cart.</th>"
        cars += "</tr>"
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
print("<title>Kristaberslo | Receipt</title>")
print("</head>")
print("<body>")
print("<br>")
print("<h1>Receipt</h1>")
print("<hr>")
print("<a href='/'>Home</a>")
print("<hr>")
print("<p><b>Order Status:</b> In Process</p>")
print("<p><b>Receipt Date:</b> " + str(receiptdate.day) + " " + str(receiptdate.strftime("%B")) + " " + str(receiptdate.year) + "</p>")
print("<br>")
print("<table>")
print("<thead>")
print("<tr>")
print("<th>QTY</th>")
print("<th>Product</th>")
print("<th>Unit Price</th>")
print("</tr>")
print("</thead>")
print("<tbody>")
print(cars)                                                             # Print all products that have been selected by the customer
print("</tbody>")
print("</table>")
print("<br>")
print("<b>Subtotal:</b> ${:,.0f}".format(price))
print("<br><br>")
print("<hr>")
print("<p>Copyright &copy; 2021 Kristaberslo AS.</p>")
print("</body>")
print("</html>")