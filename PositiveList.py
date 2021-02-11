n=int(input("Enter number of elements:"))
ele=[]
for i in range(0,n):
    ele.append(int(input()))
print("Positive list:")
for j in ele:
    if j>0:
        print(j,end=' ')
