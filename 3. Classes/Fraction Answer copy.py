class Fraction:
    def __init__(self, numerator, denominator = 1):
        self.numerator = numerator
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        self.denominator = denominator
    
    def __add__(self, other):
        #cross multiply
        new_numerator = other.denominator*self.numerator + self.denominator*other.numerator
        new_denominator = self.denominator*other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        #flip and cross multiply
        new_numerator = other.denominator*self.numerator - self.denominator*other.numerator
        new_denominator = self.denominator*other.denominator
        if new_denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    #truedive = /, div = //, mod = %
    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __str__(self): #for printing and converting to str, represent with a/b
        return str(self.numerator) + "/" + str(self.denominator)
    
    def __repr__(self): #for terminal and debugging, represent with float
        return str(self.numerator/self.denominator)


a = Fraction(3, 4)
b = Fraction(2, 7)
print(a, b)

print("\nTesting Add:")
print("a+b =", a + b)
print("b+a =", b + a)

print("\nTesting Subtract;")
print("a-b =", a - b)
print("b-a =", b - a)

print("\nTesting Multiply:")
print("a*b =", a * b)
print("b*a =", b * a)

print("\nTesting Divide:")
print("a/b =", a / b)
print("b/a =", b / a)