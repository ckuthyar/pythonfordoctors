f1=open("in8.txt","r")
f2=open("out8.txt","w")

num1=int(f1.readline())
num2=int(f1.readline())
sum1=num1+num2

print(sum1)
f2.write(str(sum1))
f2.close()

