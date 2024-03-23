import random
import datetime


current_time = datetime.datetime.now().time()
seed_value = int((current_time.second*10))
print(seed_value)
random.seed(seed_value)

print(random.randint(1, 50))
print(random.randint(1, 50))
print(random.randint(1, 50))
print(random.randint(1, 50))
print(random.randint(1, 50))




