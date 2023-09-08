#Write input 1: 1 integer, 20 <= stop_range <= 100
#Write input 2: 1 integer, 1 <= num_divisors <= 12

#Step 1
#Use range(10, stop_range) to cycle through numbers
#Find the sum of the numbers integers
    #Look at Assignment 3.5
#See if that sum squared is an integer
#Write a list of the numbers under stop_range which meet these criteria and if they do print them.

#Step 2
#Use range(10, stop_range) to cycle through numbers
#If the number mod(num_divisors) == 0 then that number works
#Print out all numbers which work

#Inputs written
input_1 = int(input())
input_2 = int(input())
if input_1 >= 20 and input_1 <= 100:
    stop_range = input_1
else:
    print("Keep input 1 between 20 <= input 1 <= 100")
    quit()
if input_2 >= 1 and input_2 <= 12:
    num_divisors = input_2
else:
    print("Keep input 2 between 1 <= input 1 <= 12")
    quit()

#Input 1 calculation. NOT FINISHED, NOT WORKING!!!
for x in range(10, stop_range):
    while x < 0:
        digit_1 = x % 10
        digit_2 = x % 10
        x = x // 10
