import re
def read(file):
    with open(file) as f:
        contents = f.read()
    f.close()
    return contents

def sanitize(input, listInput: list = [], mode: int = 0):
    if mode != 0:
        if mode == 1:
            strings = []
            constructedString = ''
            for i in listInput:
                x = re.sub(r''+i+'\(.*\)', r'', input)
                foobar = re.findall(r".*\(.*\)", x)
                foolist = []
                for y in foobar:
                    foolist.append(re.sub(r'\(.*\)','',y))
                print(foolist)
                strings.append(foolist)
            matchTerm = strings[0]
            for foo in strings:
                matchTerm = [i for i in foo if i in matchTerm]
            x = input
            for i in matchTerm:
                print(i)
                x = re.sub(r''+i, r'', x)
            print(f'whiteList={listInput}')
            return x
        elif mode == 2:
            for i in listInput:
                constructedString =re.sub(r''+i+'\(.*\)', r'', input)
            print(f'blackList={listInput}')
            return constructedString
    return input

x = re.sub(r"print\(.*\)", '', "test(blah)\ntest(blaahala)\nprint('test')\ncat('yeet')")
x = re.findall(r".*\(.*\)", x)
y = re.sub(r"cat\(.*\)", '', "test(blah)\ntest(blaahala)\nprint('test')\ncat('yeet')")
y = re.findall(r".*\(.*\)", y)

z = []
for i in x:
    if i in y:
        z.append(i)


print(x)
print(y)

exec(sanitize(read('code.txt'), ["print", "exec"], 1))
exec(sanitize(read('code.txt'), ["eval","exec"], 2))


