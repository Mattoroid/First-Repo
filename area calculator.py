import math

#global var
s = 0 #shape selectiopn
shape = '' #shape name after selection
area = 0 #shape area
closebutton = False #verifies if player wants to exit program after using it, serves as loop 
while closebutton == False:
    while s <1 or s>5:#here, we'll select the shape
        try:
            input("Inform the number to select the shape:(press enter to se the info)")
            input('1 - Square,')
            input('2 - Rectangle,')
            input('3 - Triangle,')
            (input('4 - Circle,'))
            s = int(input('5 - Quit:'))
        except ValueError: # if person informs something else than a number asked
            print('This is not a valid answer.')
            s=0

    def valuecheck(message): # checks if value is float or string 
        value = 0
        while value <1:
            try:
                value = float(input(message)) #message to ask info
            except ValueError: # if person informs something else than a number asked
                print('This is not a valid answer.')
                value = 0
        return value


#form selected/ player accepted to quit

    if s == 1: #square 
    
        shape = 'square'
        input(f'You selected {shape}.')
        side = valuecheck('inform the side of the square:')
        area = side ** 2 #defines area from square

    elif s == 2: #rectangle
        shape = 'rectangle'
        input(f'You selected {shape}.')
        length = valuecheck('Inform the length size from the rectangle:')
        width = valuecheck('Now inform the length size from the rectangle:')
        
        area = length * width #defines area from rectangle

    elif s == 3: #triangle
        shape = 'triangle'
        input(f'You selected {shape}.')
        height = valuecheck('Inform the height of the triangle:')
        base = valuecheck('Now inform the base from triangle:')
        area = (height*base)/2 #defines area from triangle

    elif s == 4: #circle
        shape = 'circle'
        input(f'You selected {shape}.')
        radius = valuecheck('Inform the radius of the circle:')

        area = math.pi*(radius**2) #defines area from circle

    elif 5: #quit
        print('have a nice day!')
        exit() #exit program

    #All info provided, time to provide answer

    input('Thanks for information provided.')
    print(f'The area of your {shape} is {round(area,2)}')  #the final answer!

    #this session is to verify if user wants to use program again
    e = ''
    while e != 'y' and e!= 'n':
        e = input('do you wanna see the area of another shape?(y/n)')
        if e == 'y':
            s = 0 # dont forget to change s again, or user will be locked on same shape forever!
            print('Ok.')
        elif e == 'n':
            print('have a nice day!')
            closebutton = True #exit program
        else:
            print('This is not a valid answer.')
    