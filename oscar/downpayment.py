# price of a house is 1M
# if a buyer has good credits 
#     they need to put down 10%
# otherwise
#     they need to put down 20%
# print the down payment

price = 1000000
has_good_credit = True

if has_good_credit:
    put_down = 0.1 * price
else:
    put_down = 0.2 * price
print(f"Dolwn payment: {put_down}")


