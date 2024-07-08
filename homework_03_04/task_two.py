import random

def get_numbers_ticket(min, max, quantity):
    lottery_numbers = random.sample(range(min, max + 1), quantity)
    return lottery_numbers
    
min = 1
max = 1000
quantity = 6

lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", lottery_numbers)

