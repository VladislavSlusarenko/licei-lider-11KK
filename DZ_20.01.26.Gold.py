a = 8.09
b = 5

if abs(a/b - b/(a-b)) < 0.001:
    print('Так')
else:
    print('Ні')