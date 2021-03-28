import re
x = "6+5"
y = "3,3"
x = re.split(r'/, |\+', x)
y = re.split(r'/,| \+', y)
print(x)
print(y)
'''
for i in range(len(x)):
    for j in range(len(y)):
        print(int(x[i])-int(y[j]))
'''