# Ask two question
# name = input('What is your name? ')
# favourite_color = input('What is your favourite color? ')
# print(name + ' Likes ' + favourite_color + " Now use ball")

# Magic 8-Ball

"""import random
name = "Sagar"
question = "Will I win the lottery?"
answer = ""
random_number = random.randint(1, 10)
print(random_number)
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"
#print(name + " asks "+ question)
if name == "":
  print("Question: " + question)
  print("Magic 8-Ball's answer: " + answer)
#else:
  #print(name + " asks: " + question)
elif question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
  print("Magic 8-Ball's answer: " + answer)
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)"""

# Ask a user their weight(pounds) and converts into kilogram and print in terminal

'''user_weight_lbs = input('User Weight (lbs): ')
user_weight_kg = 0.45 * float(user_weight_lbs)
print(round(user_weight_kg))'''

# Price of a house is $1M. If buyer has a good credit,
# they need to put down 10% otherwise they need to put down 20%.
# Print the down payment.

'''price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: {down_payment}")'''

# project weight convertor if weight in ponds than it convert in kilos or vice versa
# Solution
'''weight = int(input('Weight: '))
unit = input('(L)bs or (k)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} ponds")'''

'''Sal's Shipping--------
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. 
Sal wants to make sure that every single one of his customers has the best, 
and most affordable experience shipping their packages.
In this project, you’ll build a program that will take the weight of a package 
and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

    Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
    Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
    Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping
Weight of Package 	Price per Pound 	Flat Charge
2 lb or less 	$1.50 	$20.00
Over 2 lb but less than or equal to 6 lb 	$3.00 	$20.00
Over 6 lb but less than or equal to 10 lb 	$4.00 	$20.00
Over 10 lb 	$4.75 	$20.00
Ground Shipping Premium
Flat charge: $125.00
Drone Shipping
Weight of Package 	Price per Pound 	Flat Charge
2 lb or less 	$4.50 	$0.00
Over 2 lb but less than or equal to 6 lb 	$9.00 	$0.00
Over 6 lb but less than or equal to 10 lb 	$12.00 	$0.00
Over 10 lb 	$14.25 	$0.00

Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method 
of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.
Note that the walkthrough video for this project is slightly out of date — the walkthrough was done using a version of
this project that uses functions. Feel free to come back to the video after having been introduced to functions!
'''
'''weight = 41.5
cost_ground_premium = 125.00

if weight <= 2:
    ground_ship_charge = weight * 1.5 + 20
    drone_ship_charge = weight * 4.50
    # print(ground_ship_charge)
elif weight <= 6:
    ground_ship_charge = weight * 3 + 20
    drone_ship_charge = weight * 9
    # print(ground_ship_charge)
elif weight <= 10:
    ground_ship_charge = weight * 4 + 20
    drone_ship_charge = weight * 12
# print(ground_ship_charge)
else:
    ground_ship_charge = weight * 4.75 + 20
    drone_ship_charge = weight * 14.25
    # print(ground_ship_charge)
print(f"Cost Ground: $ {ground_ship_charge}")
print("Ground Shipping Premium $", cost_ground_premium)
print("Drone Shipping: $", drone_ship_charge)
print("")'''



'''last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
print(last_semester_gradebook)
# Your code below: 

subject = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
gradebook[-1][-1] = 98
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)'''

# for loop, list comprehention
# Question
'''Carly's Clippers
You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. 
Your job is to go through the lists of data that have been collected in the past couple of weeks. 
You will be calculating some important metrics that Carly can use to plan out the operation 
of the business for the rest of the month.
You have been provided with three lists:
    hairstyles: the names of the cuts offered at Carly’s Clippers.
    prices: the price of each hairstyle in the hairstyles list.
    last_week: the number of purchases for each hairstyle type in the last week.
Each index in hairstyles corresponds to an associated index in prices and last_week.
For example, The hairstyle "bouffant" has an associated price of 30 from the prices list, 
and was purchased 2 times in the last week as shown in the last_week list. 
Each of these elements are in the first index of their respective lists. '''

'''hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0

for price in prices:
  total_price += price
print("Total Price:",total_price)
average_price = float(total_price / len(prices))
print("Average Haircut Price:",average_price)
new_prices = [price - 5 for price in prices]
print("new_prices =", new_prices)
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue:", total_revenue)
average_daily_revenue = float(total_revenue / 7)
print("Average Daily Revenue:", average_daily_revenue)
cuts_under_30 = [hairstyles[i] for i in
  range(len(hairstyles)) if prices[i] < 30]
print(cuts_under_30)'''

'''n = [a for a in range(1, 101) if a % 2 == 0]
print(n)

l = []

for a in range(1, 101):
    if a > 1:
        for i in range(2, a):
            if (a % i) == 0:
                break
        else:
            l.append(a)
            print(l)'''

# a function that returns the sum of the first and last elements of a given list

'''def first_plus_last(lst):
    result = lst[0] + lst[-1]
    return result


print(first_plus_last([1, 2, 3, 4]))
print(first_plus_last([8, 2, 5, -8]))
print(first_plus_last([-10, 2, 3, -4]))'''




