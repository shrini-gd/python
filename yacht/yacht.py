YACHT = lambda dice: 50 if dice.count(dice[0]) == len(dice) else 0
ONES = lambda dice: dice.count(1)
TWOS = lambda dice: dice.count(2) * 2
THREES = lambda dice: dice.count(3) * 3
FOURS = lambda dice: dice.count(4) * 4
FIVES = lambda dice: dice.count(5) * 5
SIXES = lambda dice: dice.count(6) * 6
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and FOUR_OF_A_KIND(dice)==0 else 0
FOUR_OF_A_KIND = lambda dice: max(dice, key=dice.count)*4 if dice.count(max(dice, key=dice.count))>=4 else 0
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice)==list(range(1,6)) else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice)==list(range(2,7)) else 0
CHOICE = lambda dice: sum(dice)

def score(dice, category):
    return category(dice)
