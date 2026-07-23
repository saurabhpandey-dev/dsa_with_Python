lst = []
for i in range(1,101):
    if i%3==0 and i%5==0:
        lst.append('fizzbuzz')
    elif i%5==0:
        lst.append('buzz')
    elif i%3==0:
        lst.append('fizz')
    else:
        lst.append(i)

for i in lst:
    print(i)