#write a program to calculate GST tax amount from given bill amount and tax rate
bill_amount=0
gst_amount=0
bill_amount = float(input("Enter the bill amount: "))
tax_rate = float(input("Enter the GST tax rate (%): "))

gst_amount = (bill_amount * tax_rate) / 100

print("GST Tax Amount is:", gst_amount)