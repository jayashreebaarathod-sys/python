#write a program to convert given 3 digit amount into words
# input : 175 output : one seven five 

number=int(input("enter tha 3 digit number"))
first=number // 100
second=(number // 10) % 10
last=number % 10

words = ['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[first]," ",words[second],"", words[last])