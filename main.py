from func import menu,insert,showall,searchid,search,delete
loop=True
while(loop):
    menu()
    option1=input("please select...")
    option = int(option1)
    if option == 1:
        insert()
    elif option == 2:
        search()
    elif option ==3:
        delete()
    elif option == 4:
        showall()
    elif option ==0:
        print('Exiting...')
        loop=False
    else:
        print('Invalid input,please re-selecet or input 0 to exit')

    

