def load():
    list=[]
    for i in range(10):
        list.append([])
        for j in range(10):
            list[i].append('-')


    for i in range(10):
        for j in range(10):
            print(list[i][j]+' ',end="")
        print()

load()