class Point:
    def __init__(self, x, y): #defining the constructor
        self.x = x
        self.y = y

    def draw(self):
        print("draw")

    def shade(self):
        print("shade")

# creating an instance of Point 

point1 = Point(10, 20)
print(point1.x)
print(point1.y)
        