l = [1,2,2,3,5,4,4,4,4]

def check_luck(lst):
    d = {}
    for i in lst:
        if lst.count(i) == i:
            d.update({i:'lucky number'})
    print(d)
check_luck(l)
    
        
