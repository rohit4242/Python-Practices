# Write a program to input Principal Amount, Rate and Year and
# display Simple Interest.

def Simple_Interest(Amount, Rate, Year):
    return (Amount * Rate * Year) / 100


Amount = float(input("Enter Your Amount: "))
Rate = float(input("Enter Your Rate: "))
Year = float(input("Enter Your Year: "))

Interest = Simple_Interest(Amount, Rate, Year)

print("Your Simple Interest is: ", Interest)
