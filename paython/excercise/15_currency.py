#write a program to display dinominations of currency for given amount

'''
input : 887 Rupees 
output : 
500 x 1 = 500
200 x 1 = 200
100 x 1 = 100
50 x 1 =  50
20 x 1 =  20
10 x 1 =  10
5 x 1 =   05
2 x 1 =   02
1 x 1 =   01

'''
'''
amount = int(input("Enter the amount: "))


j500 = amount // 500
amount %= 500

j200 = amount // 200
amount %= 200

j100 = amount // 100
amount %= 100

j50 = amount // 50
amount %= 50

j20 = amount // 20
amount %= 20

j10 = amount // 10
amount %= 10

j5 = amount // 5
amount %= 5

j2 = amount // 2
amount %= 2

j1 = amount


print("500  :", 500)
print("200  :", 200)
print("100  :", 100)
print("50   :", 50)
print("20   :", 20)
print("10   :", 10)
print("5    :", 5)
print("2    :", 2)
print("1    :", 1)
'''
amount = int(input("Enter amount in rupees: "))

notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for note in notes:
    count = amount // note
    amount = amount % note
    print(note, "x", count, "=", note * count)