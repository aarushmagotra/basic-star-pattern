def star_normal():
# This program will print a simple star pattern
    a = int(input('Enter a number: '))
    for i in range(1, a+1):
        for j in range(1, i+1):
            print('*', end = ' ')
        print()
def star_reverse():    
# here there will be a code that will print the same pattern in reverse
    b = int(input('Enter a number: '))
    for i in range(a, 0, -1):
        for j in range(i,0, -1):
            print('*', end = ' ')
        print()
     # I add the code for you
    
def which():
    print('Code     Choice')
    print('1.>      Normal')
    print('2.>      Reverse')
    print('3.>      Quit')
    w = int(input('Enter your choice: '))
    if w == 1:
        star_normal()
    elif w == 2:
        star_reverse()
    eif w == 3:
        print('Bye!!!')
        quit()
    else:
        print ('Invalid input!!')
        print ('Try again')
        which()
if __name__ == '__main__':
    while True:
        which()
        
        
            
