# starting
print("hello world")

print("""Linux. Linux is a opensource monolithic operating system that is currently getting more and more popular""")

# comments

#this is a comment
"""

this is a multiline comment
"""

# data,variable,operator

#data-type
movie_title = "laut bercerita"
release_year = 2026
rating = 8.8
is_general_audiences= False
print("The Movie Name Is " + movie_title)

#operator
top_up_amount = 50 # nominal topup
count = 3 # jumlah berapa kali top up
discount = 2 #besar discount

#payment calc
total_payment = top_up_amount * count

total_discount = discount * count

clean_payment = total_payment - total_discount

#get payment
print("Total payment : " + str(total_payment))
print("Clean Payment : " + str(clean_payment))

# burger-store
print ( """" Burger Store Pricelist :
    1. Burger Beef : 20
    2. Burger Chicken : 25
    3. Burger Fish : 30 """)

menu_price = input ("Menu Price : ")
amount = input ("Amount : ")
bill =  int(menu_price)* int(amount)
print("you need to pay $" + str(bill))
    
# Student data

first_name = input ("Your Name : ")
major = input ("Your Major : ") 
class_code = input ("Your Class :") 

print("Student Information : " + first_name + major + class_code)
print(f"Student Information : {first_name} {major} {class_code}" )