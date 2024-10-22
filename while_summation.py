#while summation code following directions from Readme
user_num = int(input())
looped_times = 0
total = 0

while looped_times <= user_num:
    total = total + looped_times
    looped_times = looped_times + 1
print(total)
