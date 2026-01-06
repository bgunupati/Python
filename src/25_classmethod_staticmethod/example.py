class Vehicle:
    TYPES = ("Manul","Automatic")

    def __init__(self, name, transmission_type, price):
        self.name = name
        self.transmission_type = transmission_type
        self.price = price

    def __repr__(self):
        return f"<Vehicle: {self.name}, Transmission: {self.transmission_type}, Price: ${self.price}>"
    

    @classmethod
    def AutomaticTransmission(cls, name, price):
        return cls(name, cls.TYPES[0], (price * 1.1))

    @classmethod
    def MaualTransmission(cls, name, price):
        return cls(name, cls.TYPES[1],(price) )

aVehicle = Vehicle.AutomaticTransmission("Honda",35000)
mVehicle = Vehicle.MaualTransmission("Honda",35000)

print(aVehicle)
print(mVehicle)
