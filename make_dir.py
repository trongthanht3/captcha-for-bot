import os
import string

for c in string.ascii_lowercase:
    os.makedirs('train_data/' + c.upper())
for i in range(10):
    os.makedirs('train_data/' + str(i))
