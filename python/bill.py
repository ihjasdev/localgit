#print("Hi, I am a beginner in Python. ")
print ("... Welcome to Abdullah Coffee Shop...")
print ("Dear valued customer, your bill amount is below.")

Amount = int (input ("Enter the ate meal amount :$"))
sales_tax = int(input("what is the sales tax (percentage)?  "))
tip =int(input("Enter the tip in percentage: "))


tax_amount=(Amount*sales_tax)/100#calculate tax.
total=Amount+tax_amount
tip_amount = (total*tip)/100
total = tip_amount + total
total = round(total,2)#round the amount in 2 decimal place.

print("The toltal bill is $",total)

