class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.rooms} rooms, {self.area} sq. meters\nPrice: {self.price}\nAddress: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House\n{super().__str__()}\nPlot size: {self.plot} sq. meters"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat\n{super().__str__()}\nFloor: {self.floor}"


house = House(area=150, rooms=5, price=390000, address="123 Post", plot=500)
flat = Flat(area=80, rooms=3, price=150000, address="456 Lim", floor=2)


print(house)
print("\n------------------------\n")
print(flat)
