for i in range(0,6):
    for j in range(i):
        print('*',end=" ")
    print()
    print()
whc=[1,1]
i=1
while i<=18:
  add_eng=whc[-1]+whc[-2]
  whc.append(add_eng)
  i+=1
print(whc)