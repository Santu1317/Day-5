'''class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, cost):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.cost = cost
        self.premium_amount = self.calculate_premium_amount()

    def calculate_premium_amount(self):
        if self.vehicle_type == "Two Wheeler":
            return self.cost * 0.02
        elif self.vehicle_type == "Four Wheeler":
            return self.cost * 0.06
        else:
            return("Invalid vehicle type")

    def get_vehicle_id(self):
        return self.vehicle_id

    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def get_vehicle_type(self):
        return self.vehicle_type

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type
        self.premium_amount = self.calculate_premium_amount()

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost
        self.premium_amount = self.calculate_premium_amount()

    def get_premium_amount(self):
        return self.premium_amount

    def __str__(self):
        return f"Vehicle ID: {self._vehicle_id}, Vehicle Type: {self.vehicle_type}, Cost: {self.cost}, Premium Amount: {self._premium_amount}"                                                                                   
vehicle1 = Vehicle("V001", "Two Wheeler", 50000)
print(vehicle1.get_premium_amount())  
vehicle2 = Vehicle("V002", "Six Wheeler", 100000)
print(vehicle2.get_premium_amount())'''
#------------------------------------------------------------------

'''class university:
    def __init__(self,age,marks):
        self.age=age
        self.marks=marks
    def qualifying_exam(self):
       if self.age>20 and self.marks>=65:
           print("eligible")
       else:
           print("noteligible")
a=int(input("Enter your age-"))
b=int(input("Enter your mark-"))
obj1=university(a,b)
obj1.qualifying_exam()'''
#-------------------------------------------------------
           
'''class Student:
    def __init__(self, student_id, age, marks):
        self.student_id = student_id
        self.age = age
        self.marks = marks
    def is_valid(self):
        return self.age > 20 and 0 <= self.marks <= 100    
    def qualifies_for_admission(self):
        return self.is_valid() and self.marks >= 65
students = [
    Student("S1", 22, 70),
    Student("S2", 18, 50),
    Student("S3", 25, 80),
    Student("S4", 21, 60),
]
for student in students:
    if student.qualifies_for_admission():
        print(f"{student.student_id} qualifies for admission.")
    else:
        print(f"{student.student_id} does not qualify for admission.")'''
#---------------------------------------------------------------------------------

'''class student:
    def __init__(self):
        self.__id=None
        self.__marks=None
        self.__age=None
        self.__course=None
        self.__discount_price=None

    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return self.__id

    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks

    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age

    def set_course(self,course):
        self.__course=course
    def get_course(self):
        return self.__course

    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return True
        else:
            return False

    def validate_age(self,):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if (self.validate_marks()==True and self.validate_age()==True and self.__marks>=65):
            return True
        else:
            return False

    def course_selection(self,):
        if self.check_qualification()==True:
            if self.__marks>85:
                if self.__course==1001:
                    self.__discount_price=25575-25575*0.25
                elif self.__course==1002:
                    self.__discount_price = 15500 - 15500 * 0.25
            else:
                if self.__course == 1001:
                    self.__discount_price = 25575
                elif self.__course == 1002:
                    self.__discount_price = 15500
        return self.__discount_price

    def display(self):
        if self.check_qualification()==False:
            print("Student having id: ",self.__id," is not eligible for admission")
        else:
            print("Student having id: ",self.__id," is qualified and the course price is",self.__discount_price)

s1=student()
s1.set_id(101)
s1.set_age(22)
s1.set_marks(87)
s1.set_course(1001)

s1.validate_age()
s1.validate_marks()
s1.course_selection()
s1.display()'''
#-------------------------------------------------------

'''class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity
        
    def get_customer_name(self):
        return self.__customer_name
        
    def get_quantity(self):
        return self.__quantity
        
    def validate_quantity(self):
        if self._quantity>=1 and self._quantity<=5:
            return True
        return False

class Pizzaservice:
    counter=100
    def _init_(self,customer,pizza_type,additional_topping=False):
        self.__service_id=None
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=None
        
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in ["small","medium"]:
            return True
        return False
    
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            Pizzaservice.counter+=1
            if self.__pizza_type.lower()=="small":
                self.pizza_cost=150*self.__customer.get_quantity()
                if self.__additional_topping==True:
                    self.pizza_cost+=35*self.__customer.get_quantity()
                self.__service_id="S"+str(Pizzaservice.counter)
            if self.__pizza_type.lower()=="medium":
                self.pizza_cost=200*self.__customer.get_quantity()
                if self.__additional_topping==True:
                    self.pizza_cost+=50*self.__customer.get_quantity() 
                self.__service_id="M"+str(Pizzaservice.counter)
        else:
            self.pizza_cost=-1 
            
    def get_service_id(self):
        return self.__service_id
        
    def get_customer(self):
        return self.__customer
        
    def get_pizza_type(self):
        return self.__pizza_type
        
    def get_additional_topping(self):
        return self.__additional_topping
    
class Doordelivery(Pizzaservice):
    def _init_(self,customer,pizza_type,additional_topping,distance_in_kms):
        super().__init__(customer,pizza_type,additional_topping)
        self.__delivery_charge=None
        self.__distance_in_kms=distance_in_kms
        
    def validate_distance_in_kms(self):
        if self._distance_in_kms>=1 and self._distance_in_kms<=10:
            return True
        return False
    
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            if self.pizza_cost != -1:
                if self.__distance_in_kms<=5:
                    self._delivery_charge=self._distance_in_kms*5 
                else:
                    self._delivery_charge=25+(self._distance_in_kms-5)*7 
                self.pizza_cost+=self.__delivery_charge
        else:
            self.pizza_cost=-1
    
    def get_delivery_charge(self):
        return self.__delivery_charge
        
    def get_distance_in_kms(self):
        return self.__distance_in_kms'''
#---------------------------------------------------------------------------------

class Customer:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.quantity = 0

    def validate_quantity(self, quantity):
        if quantity > 0 and quantity <= 2:
            self.quantity = quantity
            return True
        else:
            return False

class PizzaService:
    counter = 100

    def __init__(self, pizza_type, additional_topping):
        self.pizza_type = pizza_type
        self.additional_topping = additional_topping
        self.pizza_cost = 0
        self.service_id = chr(ord(pizza_type[0].upper())) + str(PizzaService.counter)
        PizzaService.counter += 1

    def validate_pizza_type(self):
        if self.pizza_type.lower() == 'small' or self.pizza_type.lower() == 'medium':
            return True
        else:
            return False

    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and customer.validate_quantity(customer.quantity):
            if self.pizza_type.lower() == 'small':
                self.pizza_cost = 150
            elif self.pizza_type.lower() == 'medium':
                self.pizza_cost = 200
            if self.additional_topping:
                self.pizza_cost += 50
        else:
            self.pizza_cost = -1

class DoorDelivery(PizzaService):
    def __init__(self, pizza_type, additional_topping, distance_in_kms):
        super().__init__(pizza_type, additional_topping)
        self.distance_in_kms = distance_in_kms
        self.delivery_charge = 0

    def validate_distance_in_kms(self):
        if self.distance_in_kms >= 1 and self.distance_in_kms <= 10:
            return True
        else:
            return False

    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms() and super().validate_pizza_type() and customer.validate_quantity(customer.quantity):
            super().calculate_pizza_cost()
            if self.pizza_cost != -1:
                if self.distance_in_kms <= 5:
                    self.delivery_charge = 5
                else:
                    self.delivery_charge = 5 + (self.distance_in_kms - 5) * 7
        else:
            self.pizza_cost = -1

# Test the program
customer = Customer("John Doe", "123 Main Street", "555-1234")

# Test PizzaService
pizza_service = PizzaService("small", True)
pizza_service.calculate_pizza_cost()
print("PizzaService Details:")
print("Service ID:", pizza_service.service_id)
print("Pizza Type:", pizza_service.pizza_type)
print("Additional Topping:", pizza_service.additional_topping)
print("Pizza Cost:", pizza_service.pizza_cost)

# Test DoorDelivery
door_delivery = DoorDelivery("medium", False, 7)
door_delivery.calculate_pizza_cost()
print("DoorDelivery Details:")
print("Service ID:", door_delivery.service_id)
print("Pizza Type:", door_delivery.pizza_type)
print("Additional Topping:", door_delivery.additional_topping)
print("Distance in KMs:", door_delivery.distance_in_kms)
print("Pizza Cost:", door_delivery.pizza_cost)
print("Delivery Charge:", door_delivery.delivery_charge)
#----------------------------------------------------------------------------

