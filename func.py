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


def write(list):
    try:
        f = open('record.txt', 'a')
    except Exception as e:
        f= open('record.txt', 'w')
    f.write(str(list))
    f.close


def insert():
    insert_ctrl=True
    while(insert_ctrl):
        list1=[]
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
        list1.append('ID:'+id)
        list1.append('Name:'+name)
        list1.append('Score:'+score)
        print(list1)
        write(str(list1)+'\n')
        insert_choice = input('continue to input y/n?')
        if insert_choice == 'y':
            pass
        else:
            insert_ctrl = False
            print('Exsting Insert')

def delete():
    delete_ctrl=True
    f=open('record.txt','r')
    content=f.readlines()
    print(content)
    # while(delete_ctrl):
    #     delete_input=input('please input ID you want delete:')
        



def showall():
    f=open('record.txt','r')
    content=f.readlines()
    print(content)
    
       




    
    


    


