class Shape:
    def __init__(self, color):
      self.color = color

    def area(self):
      return 0
    
    def perimeter(self):
      return 0
    
    def __str__(self):
      return self.colors
    

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = float(width)
        self.height = float(height)

    def area(self):
       return self.width * self.height
    
    def perimeter(self):
       return 2 * self.width * self.height
    
    def __str__(self):
       return f"{self.color} rectangle with width {self.width} and height {self.height}"


rectangle = Rectangle("red", 5, 10)
print(rectangle)

