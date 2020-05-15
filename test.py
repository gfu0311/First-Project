# f=open('test.txt','w')
# i=1
# while i<10:
# f.write(str(i)+'\n')
# i=i+1
# f.close()


f=open('test.txt','r')
content = f.readlines()
print(content)
for list in content:
    print(list)

