#write a program to convert given minutes into hours and remaining minutes
#input : 150 minutes  , output : 2 hours and 30 minutes

time = input("Enter the minutes")
time = int(time)

hours = time //60
minutes = time % 60 

print(hours,"hours",minutes,"minutes")