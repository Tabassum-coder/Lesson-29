class Vehicle:

    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    
class Bus(Vehicle):
    pass

bus=Bus('School Volvo','200','12')
print("Name of bus is ",bus.name)
print("Maximum speed is ",bus.max_speed+" with mileage of ",bus.mileage)