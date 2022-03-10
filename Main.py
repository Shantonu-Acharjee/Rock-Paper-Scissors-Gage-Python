from random import randint
#RandomNumber = randint(1,3)


a = ['Rock', 'Paper', 'Seissors'] 

try:
    print('1 : Rock \n2 : Paper \n3 : Seissors')
    UserInput = int(input('Now your trun : '))
    print('You Enter ', a[UserInput - 1])

except:
    print('Plese Enter Valid Vlue')


    



def b(UserInput):
    RandomNumber = randint(1,3)
    RandomNumber = RandomNumber - 1


    if UserInput == UserInput:
        #print('Random Number is : ', RandomNumber)

        if RandomNumber == 0:
            computer =  a[RandomNumber]
            print('Computer : ', computer)
            

        elif RandomNumber == 1:
            computer =  a[RandomNumber]
            print('Computer : ', computer)
            

        elif RandomNumber == 2:
            computer =  a[RandomNumber]
            print('Computer : ', computer)
            


    if RandomNumber == 0: # rock
        
        if UserInput-1 == 0:
            print('Drow') 
        

        elif UserInput-1 == 1:
            print('You Win')

        elif UserInput-1 == 2:
            print('Computer Win')



    elif RandomNumber == 1: # paper
        
        if UserInput-1 == 0:
            print('Computer win') 
        

        elif UserInput-1 == 1:
            print('Drow')

        elif UserInput-1 == 2:
            print('You Win')




    elif RandomNumber == 2: # Seissors
        
        if UserInput-1 == 0:
            print('You Win') 
        

        elif UserInput-1 == 1:
            print('Computer Win')

        elif UserInput-1 == 2:
            print('Drow')


            

b(UserInput)








