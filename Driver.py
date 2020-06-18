from Customer import *
from Reservation import *
#function to check the availability of an airline booking class requested by customer and if it is not available system will return a lesser class
def bookingAirline(customer,airlines):
    bookingMade = False
    #prioirty dictionary to get the next lesser class
    priority = {'First': ['Business', 'Economy'], 'Business': ['Economy'], 'Economy': []}
    booking_class = customer.get_airline_class_preference()
    classChosen=''
    airlineChosen=''
    price=0.0
    for airline in airlines:
        if bookingMade == False:
            if airline.is_available(booking_class):
                classChosen=booking_class
                airlineChosen=airline._name
                price=airline.get_price(booking_class)
                break
            else:
                for p in priority[booking_class]:
                    if airline.is_available(p):
                        classChosen=p
                        airlineChosen=airline._name
                        bookingMade = True
                        price=airline.get_price(p)
                        break
    return classChosen,airlineChosen,price

#function to check the availability of a hotel booking class requested by customer and if it is not available system will return a lesser class
def bookingHotel(customer, hotels):
    hotelClassChoosen =''
    hotelChoosen =''
    price =0.0
    booking_class = customer.get_hotel_class_preference()
    # prioirty dictionary to get the next lesser class
    hotelPriority = {'Penthouse': ['Business', 'Standard'], 'Business': ['Standard'], 'Standard': []}
    hotelBooked = False
    for hotel in hotels:
        if hotelBooked == False:
            if hotel.is_available(booking_class):
                hotelClassChoosen = booking_class
                hotelChoosen = hotel._name
                price = hotel.get_price(booking_class)
                break
            else:
                for p in hotelPriority[booking_class]:
                    if hotel.is_available(p):
                        hotelClassChoosen = p
                        hotelChoosen = hotel._name
                        hotelBooked = True
                        price = hotel.get_price(p)
                        break
    return hotelClassChoosen,hotelChoosen,price
#pre defined function to calculate costs for all possible combinations of airline and hotel and checking for availability before adding it in the final dict
def calValues(airlines,hotels):
    allvalues ={}
    for airline in airlines:
        for hotel in hotels:

            allPricesAirlies = airline.get_prices()
            allPriceHotels = hotel.get_prices()
            for i in allPricesAirlies:
                for j in allPriceHotels:
                    if allPricesAirlies[i]+allPriceHotels[j] != 0 and airline.is_available(i) and hotel.is_available(j):
                        allvalues.update({airline._name+"join"+hotel._name+"join"+i+"join"+j:allPricesAirlies[i]+allPriceHotels[j]})
                    else:
                        continue
    return allvalues
#function to get another booking in the budget range when the user requested booking choice does not fit the customer budget

def getAnotherBookinginRange(calculatedValues,customerBudget):

    anotherBookingFound = False
    for i in range(0, len(calculatedValues)):
        valuetocompare = list(calculatedValues.values())[i]
        if customerBudget <= valuetocompare:
            i += 1
        else:
            reqValue = valuetocompare
            reqKey = list(calculatedValues.keys())[i]
            anotherBookingFound = True
            break
    if anotherBookingFound == True:
        return (reqValue,reqKey)
    else:
        return anotherBookingFound
#Have added another attribute to customer object - Budget
def driver():

    airlines = [Airline('Spirit'), Airline('United')]
    hotels = [Hotel('Four Seasons'), Hotel('Marriott')]
    customers = [Customer('George', 'Washington', Airline.CLASS_BUSINESS, Hotel.CLASS_STANDARD,3000),
                 Customer('Thomas', 'Jefferson', Airline.CLASS_FIRST, Hotel.CLASS_STANDARD,3000),
                 Customer('James', 'Madison', Airline.CLASS_FIRST, Hotel.CLASS_BUSINESS,2000),
                 Customer('Andrew', 'Jackson', Airline.CLASS_BUSINESS, Hotel.CLASS_PENTHOUSE,3000),
                 Customer('Abraham', 'Lincoln', Airline.CLASS_BUSINESS, Hotel.CLASS_STANDARD,200),
                 Customer('Theodore', 'Roosevelt', Airline.CLASS_ECONOMY, Hotel.CLASS_PENTHOUSE,300),
                 Customer('Woodrow', 'Wilson', Airline.CLASS_FIRST, Hotel.CLASS_PENTHOUSE,700),
                 Customer('Franklin', 'Roosevelt', Airline.CLASS_BUSINESS, Hotel.CLASS_STANDARD,500),
                 Customer('Harry', 'Truman', Airline.CLASS_BUSINESS, Hotel.CLASS_STANDARD,450),
                 Customer('John', 'Kennedy', Airline.CLASS_ECONOMY, Hotel.CLASS_BUSINESS,12)]

    for customer in customers:
        calculatedValues = calValues(airlines, hotels)
        tup=bookingAirline(customer,airlines)
        tup1 = bookingHotel(customer, hotels)
        customerPrefeerredCost = tup[2] +tup1[2]
        if customerPrefeerredCost > customer.budget:
            if bool(getAnotherBookinginRange(calculatedValues,customer.budget)) == False:
                print("Please find your booking details:")
                print("hi"+" "+customer.customer_record['Customer Name']+" "+",Please come back again as no booking is in your budget")
                print("You can contact the representative to update your budget if you wish")
                print(" ")
            else:
                tup3 = getAnotherBookinginRange(calculatedValues,customer.budget)
                reqValue = tup3[0]
                reqKey = tup3[1]
                modifiedAirlinesandClasses = reqKey.split("join")
                if modifiedAirlinesandClasses[0] == "Spirit":
                    airlines[0].make_reservation(customer,str(modifiedAirlinesandClasses[2]))
                else:
                    airlines[1].make_reservation(customer, str(modifiedAirlinesandClasses[2]))
                if modifiedAirlinesandClasses[1] == "Four Seasons":
                    hotels[0].make_reservation(customer, str(modifiedAirlinesandClasses[3]))
                else:
                    hotels[1].make_reservation(customer, str(modifiedAirlinesandClasses[3]))
                customer.customer_record['Cost'] = reqValue
                print("Please find your booking details:")
                customer.print_record()
                print(" ")
        else:
            for airline in airlines:
                if airline._name == tup[1]:
                    customer.set_airline_class_preference(tup[1])
                    airline.make_reservation(customer, str(tup[0]))
                    break
                else:
                    continue
            for hotel in hotels:
                if hotel._name == tup1[1]:
                    customer.set_hotel_class_preference(tup1[1])
                    hotel.make_reservation(customer, str(tup1[0]))
                    break
                else:
                    continue
            customer.customer_record['Cost'] = customerPrefeerredCost
            print("Please find your booking details:")
            customer.print_record()
            print(" ")


if __name__ == '__main__':
    driver()
