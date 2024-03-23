s = "Hi Sanjay"

print(type(s))  # get type of identifier
print(id(s)) # id in the memory
print(s[1:-1])  # print from 1st till 2nd last items
print(s[:-1])  # extract from beginning to end -1
print(s[:])  # extract all
print(s[1:])  # exclude 0th item and print till end.
print(s.split(' ')) # Split by space  ['Hi', 'Sanjay']
print((s.split("a"))) # split by char ['Hi S', 'nj', 'y']

print('a' in s)  # print true
print('z' in s) # print false

