
def check(n):
    i=0
    while(i*i<=n):
        if i*i == n:
            print('its perfect!!')
            return
        i+=1
    print('it\'s not')


n = int(input('Enter the number'))
check(n)