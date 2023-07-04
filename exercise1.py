#First exercise, creating a variable, collecting input fro user and printing the output 
#This is a new copy from the local file to gitHub!!
ice_cream_rating = int(input("Enter ice cream rating between 0 and 10: "));
sleeping_rating = int(input("Enter your sleeping rating between 0 and 10: "))

happiness_rating = (ice_cream_rating + sleeping_rating)/2
rating_percent = happiness_rating*10
   
#Name variable
first_name = str(input("Your first name: "))
last_name = str(input("Your last name: " ))
my_name = first_name + last_name

#Output of inputs
print("My name is ", my_name, "my ice cream rating is ", ice_cream_rating)
print("My sleeping rating is ", sleeping_rating, " out of 10")
print("Based on the factors above, my happiness rating is :", happiness_rating, " out of 10, or ", rating_percent, "%")

