#distance formula
def distance(x,y,xx,yy):
    return ( ((x-xx)**2+(y-yy)**2)**(1/2) )

class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def setMagnitude(self, magnitude):
        self.normalize()
        self.x = self.x * magnitude
        self.y = self.y * magnitude

    def normalize(self):
        scale = self.magnitude()
        if scale != 0:
            self.x = self.x / scale
            self.y = self.y / scale

    def magnitude(self):
        return( (self.x**2 + self.y**2)**(1/2) )
    #operator overloads
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return vector(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return vector(self.x / other.x, self.y / other.y)
