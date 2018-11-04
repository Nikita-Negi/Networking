a=[]
n = int(input('Enter the number of bits'))
powers_2 = []
for i in range(n):
    print("Enter data(4 bit binary) for position ",i)
    a.append(input())
    if(i<8):
        powers_2.append(pow(2,i))

data=[]
parity=[]
q=0
for i in range(100):
    data.append("x")
for i in range(n):
    if(i in powers_2):
        print(i)
        data[i]=("?")
        n+=1
    else:
        data[i]=a[q]
        q+=1

for i in range(n):
    if(data[i]!="x"):
        if i in powers_2:
            x=int(powers_2.index(i))
            print("x=",x)
            for j in range(n):
                if(j==0):
                    parity=int(data[j][3-x])
                if(j not in powers_2 and data[j]!="?" and data[j]!="x"):
                    print(data[j][3-x])
                    parity^=int(data[j][3-x])
            data[i]=parity

            print("parity bit",x," ",data[i])


for i in range(n):
    if(data[i]!="x"):
        print(data[i])
