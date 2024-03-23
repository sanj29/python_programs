s = "Welcome to python 123123ab"
s_upper = s.upper().replace(" ", "") + "21345"

print(s.upper())
print(s.lower())
print(s.isalnum())
print(s.islower())

print(s_upper)
print(s_upper.isupper())
print(s_upper.isalnum())
print(s.isalpha())

print(s.swapcase())
print(s_upper.swapcase())

print(s.startswith("Wel"))
print(s.endswith("ab"))

stm = " Hi i am programmer "

print(stm.lstrip())  # remove space from left
print(stm.rstrip())  # remove space from right
print(stm.split(" ")) # split based on space
print(stm.strip())  # remove left n right spaces
print(stm.partition("a")) # partitions string into 3 parts based on first occurrence of specified string
