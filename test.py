# f=open('test.txt','w')
# i=1
# while i<10:
# f.write(str(i)+'\n')
# i=i+1
# f.close()


# f=open('test.txt','r')
# content = f.readlines()
# print(content)
# for list in content:
#     print(list)

# list1=[5, 3, 6, 8, 0, 1]
# print(list1)
# n=1
# while n<6:
#     for i in range(5):
#         if list1[i]>list1[i+1]:
#             list1[i],list1[i+1] = list1[i+1],list1[i]
#             print(list1)
#     n=n+1
# print(list1)

# f=open('record.txt','r')
# list1=[]
# content=f.readlines()
# for item in content:
#     dict1=eval(item)
#     list1.append(dict1)
# print(list1)
# list1.sort(key=lambda content:content['ID'])
# print(list1)
# n=len(list1)
# print(n)
# for i in range(n):
#     print(list1[i])

x=2
y=3
print(lambda x,y:x*y)

