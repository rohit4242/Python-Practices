# Write a Python Program accept comma separated string and
# display tokens using split(), rsplit() and splitlines()


num = input("Enter a sequence of comma-separated numbers: ")

A = num.split(',')
B = num.rsplit(',', 1)
C = num.splitlines()

print("Your String A is ", A)
print("Your String B is ", B)
print("Your String C is ", C)
