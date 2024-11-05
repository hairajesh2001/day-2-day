class Dimension:
        def __init__(self, inches): #convert given inches into feet and inches
            if inches >= 0:
               self.feet = inches // 12
               self.inches = inches % 12
            else:
                self.feet = -1
                self.inches = -1

# Examples
dim = Dimension(48)
print("Dimension feet =", dim.feet)    # Output: 2
print("Dimension inches =", dim.inches)  # Output: 1

d2 = Dimension(24)
print("Dimension feet =", d2.feet)    # Output: -1
print("Dimension  inches =",d2.inches)  # Output: -1
