
def swap_number(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return a,b


x = 5
y = 3

print("Before Swap x= {} and y= {}".format(x, y))
x, y = swap_number(x, y)
print("After Swap x is {} and y is {}".format(x, y))
