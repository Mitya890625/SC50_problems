import emoji
def main():
    emojize()
    
def emojize():
    while True:
        data = input('Input: ')
        print('Output: ' + emoji.emojize(data))
        if data == 'q':
            return
    
    
main()