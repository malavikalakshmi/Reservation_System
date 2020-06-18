import random


class Reservation(object):
    def __init__(self, name):
        self._name = name

    def is_available(self, booking_class):
        return self.get_items(booking_class) > 0

    def make_reservation(self, customer, booking_class):
        if self.is_available(booking_class):
            self.decrement_items(booking_class)
        #customer.customer_record['Cost'] += self.get_price(booking_class)
            customer.customer_record['Reservation Id'][self._name] = \
                self.get_id_prefix() + str(random.randrange(1000000, 2000000, 1))

    def get_items(self, booking_class):
        raise NotImplementedError

    def decrement_items(self, booking_class):
        raise NotImplementedError

    def get_id_prefix(self):
        raise NotImplementedError

    def get_price(self, booking_class):
        raise NotImplementedError


class Airline(Reservation):
    CLASS_FIRST = 'First'
    CLASS_BUSINESS = 'Business'
    CLASS_ECONOMY = 'Economy'

    def __init__(self, name):
        super(Airline, self).__init__(name)

        if self._name == 'United':
            self.seats = {
                self.CLASS_FIRST: 4,
                self.CLASS_BUSINESS: 2,
                self.CLASS_ECONOMY: 0,
            }
            self.prices = {
                self.CLASS_FIRST: 2000,
                self.CLASS_BUSINESS: 750,
                self.CLASS_ECONOMY: 300,
            }
        if self._name == 'Spirit':
            self.seats = {
                self.CLASS_FIRST: 0,
                self.CLASS_BUSINESS: 0,
                self.CLASS_ECONOMY: 32,
            }
            self.prices = {
                self.CLASS_FIRST: 0,
                self.CLASS_BUSINESS: 0,
                self.CLASS_ECONOMY: 175,
            }

    def get_items(self, booking_class):
        return self.seats[booking_class]

    def decrement_items(self, booking_class):
        self.seats[booking_class] -= 1

    def get_id_prefix(self):
        return str(self._name + '_').upper()

    def get_prices(self):
        return self.prices

    def get_price(self, booking_class):
        return self.prices[booking_class]


class Hotel(Reservation):
    CLASS_PENTHOUSE = 'Penthouse'
    CLASS_BUSINESS = 'Business'
    CLASS_STANDARD = 'Standard'

    def __init__(self, name):
        super(Hotel, self).__init__(name)

        if self._name == 'Four Seasons':
            self.seats = {
                self.CLASS_PENTHOUSE: 0,
                self.CLASS_BUSINESS: 4,
                self.CLASS_STANDARD: 10,
            }
            self.prices = {
                self.CLASS_PENTHOUSE: 1200,
                self.CLASS_BUSINESS: 400,
                self.CLASS_STANDARD: 200,
            }
        if self._name == 'Marriott':
            self.seats = {
                self.CLASS_PENTHOUSE: 2,
                self.CLASS_BUSINESS: 12,
                self.CLASS_STANDARD: 40,
            }
            self.prices = {
                self.CLASS_PENTHOUSE: 0,
                self.CLASS_BUSINESS: 325,
                self.CLASS_STANDARD: 145,
            }

    def get_items(self, booking_class):
        return self.seats[booking_class]

    def decrement_items(self, booking_class):
        self.seats[booking_class] -= 1

    def get_id_prefix(self):
        return str(self._name + '_').upper()

    def get_prices(self):
        return self.prices

    def get_price(self, booking_class):
        return self.prices[booking_class]

