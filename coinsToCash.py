piggyBank = {
    "pennies": 342,
    "nickels": 9,
    "dimes": 32
}

def calc_dollars (bank):
    totalAmount = 0
    totalAmount += (bank['pennies'])
    totalAmount += (bank['nickels'] * 5)
    totalAmount += (bank['dimes'] * 10)
    return totalAmount/100

print(calc_dollars(piggyBank))    



