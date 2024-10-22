#while summation code following directions from Readme
user_num = int(input("What number? "))
looped_times = 0
total = 0

while looped_times <= user_num:
    print(looped_times)
    looped_times = looped_times + 1
    total = total + looped_times
print("Sum: "+ str(total))
