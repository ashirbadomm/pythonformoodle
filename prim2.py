amt=int(input("enter the gross amount of purchase"))
vat=int(input("enter the vat percentage"))
vat_amount=amt*(vat/100)
print("the vat amount is:",vat_amount)
net_amount=amt+vat_amount
print("the computed net amount is:",net_amount)
