n=int(input("Nhập số phần tử:"))  #câu a
B=[]
for i in range (0,n):
    i=int(input("Nhập phần tử x:"))
    B.append(i)
print(B)

print("Phần tử lớn nhất của dãy là:", max(B))  #câu b

print("Phần tử nhỏ nhất của dãy là:", min(B))  #câu c
print ("Chỉ số nhỏ nhất của nó là", B.index(min(B)))
