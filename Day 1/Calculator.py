import sys
import re

def add(x,y):
    if x > 0:
        return add(x-1,y+1)
    if x < 0:
        return add(x+1,y-1)
    return y

def sub(x,y):
    if y > 0:
        return sub(x-1, y-1)
    if y < 0:
        return sub(x+1, y+1)
    return x

def mult(x,y):
    if x > 0:
        return add(y,mult(x-1,y))
    if x == 0:
        return y-y

def replace(x):
    match = re.search(r'[-\+]', x)
    if re.search(r'(.*)(-)([0-9]*)', x) is not None and match[0] == "-":
        return replace(re.sub(r'(.*)(-)([0-9]*)', r'sub(\g<1>,\g<3>)', x))
    if re.search(r'(.*)(\+)([0-9]*)', x) is not None and match[0] == "+":
        return replace(re.sub(r'(.*)(\+)([0-9]*)', r'add(\g<1>,\g<3>)', x))
    return x

match = re.search(r'(.*)(-)([0-9]*)', sys.argv[1:][0])[2]
print(replace(sys.argv[1:][0]))
print(eval(replace(sys.argv[1:][0])))

