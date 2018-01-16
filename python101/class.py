#
x = "mike"
print(dir(x))

# create class
# python 2.x


class Vehiche(object):
    """docstring"""

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        """
        stop the car
        """
        return "%s braking" % self.vtype

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving!"

# python 3.x
# class Vehicle:
# 	"""docstring"""


# 	def __init__(self):
# 		"""Contructor"""
# 		pass

if __name__ == "__main__":
    car = Vehiche("Blue", 5, 4, "car")
    print(car.brake())
