import os
def menu():
    print("""
———————————————————学生信息管理系统———————————————|
|                                                |
| =====================功能菜单===================|
|                                                |
| 1.录入学生信息                                  | 
| 2.查找学生信息                                  |
| 3.删除学生信息                                  |
| 4.查看所有学生信息                              |
| 0.退出
""")


def write(str1):
    try:
        f = open('record.txt', 'a')
    except Exception as e:
        f= open('record.txt', 'w')
    f.write(str(str1))
    f.write('\n')
    f.close

def overwrite(str1):
    try:
        f = open('record.txt', 'w')
    except Exception as e:
        f= open('record.txt', 'w')
    f.write(str(str1))
    f.write('\n')
    f.close


def insert():
    insert_ctrl=True
    while(insert_ctrl):
        list1=[]
        dict1={}
        id=input('please input student id:')
        #check if digit if str.isdigit():
        if not id:
            check = input('invalid student id, retry? y/n')
            if check == 'y':
                continue
            else:
                break
            
        name=input('please input student name:')
        score=input('please input student score:')
        dict1={'ID':id,'Name':name,'Score':score}
        # list1.append(dict1)
        # list1.append('ID:'+id)
        # list1.append('Name:'+name)
        # list1.append('Score:'+score)
        print(dict1)
        write(dict1)
        insert_choice = input('continue to input y/n?')
        if insert_choice == 'y':
            pass
        else:
            insert_ctrl = False
            print('Exsting Insert')

def delete():
    delete_ctrl=True
    delete_a=input('please input the student ID you want to delet: ')
    f=open('record.txt','r')
    content=f.readlines()
    f.close()
    f=open('record')
    for item in content:
        dict1=eval(item)
        if dict1['ID'] == delete_a:
            pass
        else:
            write(dict1)
    
    

def pause():
    os.system('pause')
        



def showall():
    f=open('record.txt','r')
    content=f.readlines()
    for item in content:
        dict1=eval(item)
        print(dict1)
    pause()

def searchid(id):
    f=open('record.txt','r')
    content=f.readlines()
    for item in content:
        dict1=eval(item)
        if dict1['ID'] == id:
            return(item)



def search():
    ctrl=True
    while(ctrl):
        search_a=input('please input the student ID you want to search:')
        item1=searchid(search_a)
        if item1:
            print(item1)
        else:
            print('Invalid student id')
            search_b=input('continue to search y/n?: ')
            if search_b == 'y':
                continue
            else:
                ctrl=False
    pause()

    
       




    
    


    


