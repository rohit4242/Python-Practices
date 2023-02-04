# Write a program to input Principal Amount, Rate and Year and
# display Compound Interest

def Simple_Interest(Amount, Rate, Year):
    return Amount * (1 + Rate / 100) ** Year - Amount


Amount = float(input("Enter Your Amount: "))
Rate = float(input("Enter Your Rate: "))
Year = float(input("Enter Your Year: "))

Interest = Simple_Interest(Amount, Rate, Year)

print("Your Simple Interest is: ", Interest)
