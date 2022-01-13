n=int(input("Nhập số phần tử:"))
B=[]
for i in range (0,n):
    i=int(input("Nhập phần tử x:"))
    B.append(i)
print(B)

print("Phần tử lớn nhất của dãy là:", max(B))

print("Phần tử nhỏ nhất của dãy là:", min(B))
print ("Chỉ số nhỏ nhất của nó là", B.index(min(B)))
