s1 = 'Bring It On'
s2 = ' Flanked by spaces on either side '
s3 = r'C:\Users\Sanjay\Document'

print(s1.upper())
print(s1.lower())
print(s1.capitalize())
print(s1.swapcase())
print(s1.find("I"))
print(s1.find("On"))

print(s1.replace("It" ,"Him"))

print(s2.lstrip())
print(s2.rstrip())

print(s3.split("\\"))
print(s3.partition("\\"))