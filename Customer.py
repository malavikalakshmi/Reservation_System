class Customer(object):
    __id = 0

    def __init__(self, first_name, last_name, airline_class_preference, hotel_class_preference,budget):
        Customer.__id += 1
        self.__id = Customer.__id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__airline_class_preference = airline_class_preference
        self.__hotel_class_preference = hotel_class_preference
        self.__class = None
        self.__cost = 0.0
        self.budget=budget
        self.customer_record = {'Customer Name': self.__first_name + ' ' + self.__last_name,
                                'Customer Id': self.__id,
                                'Cost': self.__cost,
                                'Reservation Id': {}
                                }

    def get_airline_class_preference(self):
        return self.__airline_class_preference

    def get_hotel_class_preference(self):
        return self.__hotel_class_preference
   #setter methods
    def set_airline_class_preference(self,airline_class_preference):
        self.__airline_class_preference = airline_class_preference
   #setter methods
    def set_hotel_class_preference(self,hotel_class_preference):
        self.__hotel_class_preference = hotel_class_preference

    def print_record(self):
        record = ''
        for k, v in self.customer_record.items():
            record += f'{k}:{v} \t'
        print(record)