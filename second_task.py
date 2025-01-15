import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if not (min >= 0 and min < max <= 1000 and (max - min) >= quantity):
        return []
    else:
        nums = set()
        while len(nums) != quantity:
            nums.add(random.randint(min, max))
    return list(nums)


lottery_numbers = get_numbers_ticket(10, 15, 7)
print("Ваші лотерейні числа:", lottery_numbers)
