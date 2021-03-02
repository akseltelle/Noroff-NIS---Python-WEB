class Motorcycle:

    class Ducati:
        id = "Ducati"
        name = "Ducati 749"
        category = "Motorcycle"
        price = 11995.00
        price_2 = 23990.00
        price_3 = 35985.00
        available = "3"
        image = "/assets/images/ducati749.jpg"
        description = """
        The 749's desmo V-twin, even in base 749 guise, makes the same kind of power figures that the original 916 
        claimed, so it is far from a slow engine and certainly not one to be dismissed. Due to its smaller capacity 
        it lacks the thumping mid-range hit you get on the 999 but it still has plenty of drive and once you get 
        over the stutter at low revs (it's a big capacity V-twin, they all do that but is less pronounced than on 
        the 999...) and into the meat of the mid-range it is a lovely engine to ride. Some claim the 749 is revvier 
        than the 999, which is down to the fact it isn't as powerful and therefore you need to work it a bit harder 
        to achieve the same speeds, but it is far from rev-happy and is still a lazy and deceptively fast desmo 
        V-twin with a glorious soundtrack. The S version in both generations makes noticeably more power 
        and torque, however for road use the base 749's engine is far from lacking and most riders will be more 
        than happy with its performance.
        """


class Car:

    class Lamborghini:
        id = "Lamborghini"
        name = "Lamborghini Aventador LP750-4"
        category = "Car"
        price = 320858.00
        price_2 = 641716.00
        price_3 = 962574.00
        price_4 = 1283432.00
        price_5 = 1604290.00
        available = "5"
        image = "/assets/images/lamborghini-lp-750-4.jpg"
        description = """
        The groundbreaking innovations we introduced with the Aventador marked the beginning of a new era for super
        sports cars. With the Aventador SV Coupe we have completely redefined the concept. The Superveloce has been
        designed as the sportiest Lamborghini ever, thanks to a further improved naturally aspirated V12 engine,
        engineering solutions geared to extreme lightness, and a mix of innovative technological features,
        such as the magnetorheological push-rod suspension and the Lamborghini Dynamic Steering system. Every 
        element of the SV has been developed following the "Design to Weight" concept, with the lowest possible 
        weight and highest possible performance, to make it the fastest and most exciting Lamborghini of all time. 
        A super sports car in its purest form. Here are all the features and the technical specifications for the 
        Lamborghini Aventador Superveloce Coupe.
        """

    class Ferrari:
        id = "Ferrari"
        name = "Ferrari 360 Spider"
        category = "Car"
        price = 120000.00
        price_2 = 240000.00
        available = "2"
        image = "/assets/images/ferrari-360spider.jpg"
        description = """
        The Ferrari 360 Spider is Ferrari's 20th road-going convertible. 2,389 Ferrari 360 Spider models were built 
        for the US Market, with 670 being produced with the gated 6-speed manual transmission. The 360 Spider was the 
        best Maranello built in the time period in terms of technical content, styling, and performance, so to purchase 
        a Ferrari 360 Spider for sale is to own a crucial touchpoint in the development of the modern Prancing Horse.
        """


class Error:

    class Null:
        id = ""
        name = "This product does not exist"
        category = ""
        price = 0.00
        available = "0"
        image = "/assets/images/null.png"
        description = ""
