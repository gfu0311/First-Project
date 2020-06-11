x=0
y=0
current_player='*'
play=True


def load():
    list=[]
    for i in range(10):
        list.append([])
        for j in range(10):
            list[i].append('-')

    print('',0,1,2,3,4,5,6,7,8,9)
    for i in range(10):
        print(i,end='')
        for j in range(10):
            print(list[i][j]+' ',end="")
        print()
        
def reload(list):
    print('',0,1,2,3,4,5,6,7,8,9)
    for i in range(10):
        print(i,end='')
        for j in range(10):
            print(list[i][j]+' ',end="")
        print()


def checkerboard():
    list=[]
    for i in range(10):
        list.append([])
        for j in range(10):
            list[i].append('-')
    return list

def getchess():
    list=checkerboard()
    print(list[x][y])

def check():
    pass

def main():
    load()
    list2=checkerboard()
    global play
    while play:
        print(current_player+ ' is current player')
        input1=input('please input chess:')
        list1=list(input1)
        print(list1)
        global x, y 
        x = list1[0]
        y = list1[1]
        x=int(x)
        y=int(y)
        list2[x][y]=current_player
        reload(list2)
        print(list2[x][y])
        print(list2[x][y+1])
        print(y+1)
        # if list2[x][y] == current_player and list2[x][y+1] == current_player and list2[x][y+2] == current_player:
        if list2[x][y] == current_player and list2[x][y+1] == current_player:
            print('win')
            play=False

    
    

main()


