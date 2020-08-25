#If else
x=int(input('Enter a your Age\n'))
if(x>18 and x<25):
    print("You are eligible")
elif (x>18 and x<25):
    print("Adult")
elif(x>18 and x<50):
    print("Gents")
elif(x>18 and x<75):
    print("Citizen")
else:
    print('Senior citizen')
