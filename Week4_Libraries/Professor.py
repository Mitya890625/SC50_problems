from random import randint
def main():
    x = 0
    y = 0
    count = 0
    temp = get_level()
    for i in range(10):
        if temp == 3:
            x = randint(1, temp*333)
            y = randint(1, temp*333)
        elif temp == 2:
            x = randint(1, temp*50)
            y = randint(1, temp*50)
        elif temp == 1:
            x = randint(1, temp*10)
            y = randint(1, temp*10)
        else:
            print('invalid level')
        sum_comp = x+y
        print(str(x), '+', str(y), '= ', end='')
        user_sum = int(input())
        if user_sum == sum_comp:
            count +=1 
        else:
            print('EEE')
            for j in range(2):
                print(str(x), '+', str(y), '= ', end='')
                user_sum = int(input())
                if user_sum == sum_comp:
                    count += 1
                    break
                else:
                    print('EEE')
                if j==1:
                    print(str(x), '+', str(y), '=', str(sum_comp))
    print('Score: ',count)
    
    
def get_level():
    level = int(input('level: '))
    if level > 3:
        pass
    else:
        return level
    
    
    
main()