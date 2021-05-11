class Rectangle:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    def volume_calculation(self):
        return self.length * self.height * self.width