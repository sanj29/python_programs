import math

del_to_kol = 1050.5
print(type(del_to_kol))

print("Distance from del to kol in KM {}".format(del_to_kol))

meter = del_to_kol * 1000
feet = del_to_kol * 3280.84
inch = del_to_kol * 39370.1
cm = del_to_kol * 10000
print("Distance from del to kol in Meter is {}".format(meter))
print("Distance from del to kol in Feet is {}".format(feet))
print("Distance from del to kol in Inches is {}".format(inch))
print("Distance from del to kol in CM is {}".format(cm))

a = 2 + 3j

print(a.imag, a.real)
print(a.conjugate())
print(int('1100001110', 2))
print(int('314', 8))
print(int('34567', 16))

print(int(4.33))
print(math.ceil(16.7844))
print(math.ceil(3.555))

print(3.35 % 1.22)
print(9 % 2)
