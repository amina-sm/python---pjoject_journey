print("welcome to tip calculator")
bill=float(input("What is the total bill? $  "))
percentage_tip=int(input("What percentage tip would you like to give? 10,12 0r 15? "))
each_percentage= percentage_tip/100
total_amount= bill * each_percentage
total_amount_sum= total_amount + bill

# print(total_amount)

people=int(input("How many people to split  the bill? "))

bill_payed_each= total_amount_sum/people
final_amount=round(bill_payed_each,2)
print(f"Each person should pay: $ {final_amount} ")