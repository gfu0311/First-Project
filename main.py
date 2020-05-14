from func import menu,insert
loop=True
while(loop):
    menu()
    option1=input("please select...")
    option = int(option1)
    if option == 1:
        insert()
    elif option == 2:
        print(2)
    elif option ==3:
        print(3)
    elif option ==0:
        print('Exiting...')
        loop=False
    else:
        print('Invalid input,please re-selecet or input 0 to exit')

    

