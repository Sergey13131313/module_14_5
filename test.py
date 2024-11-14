
try:
    f = open('file.txt', 'r')
    print('Открыт')
except:
    print('Фиг!')

try:
    with open('file.txt', 'r') as ff:
        print('Открыт')
except:
    print('Фиг!')
