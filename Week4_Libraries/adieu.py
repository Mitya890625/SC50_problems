import inflect
p = inflect.engine()
myList = []
while True:
        a = input('Name: ')
        if a !='':
            myList.append(a)
        else:
            break
        
arr = p.join(myList)
print('adieu, adieu to ' + arr)