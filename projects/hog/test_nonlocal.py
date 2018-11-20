from random import randint
def func():
    index = 0
    print("func",index,id(index))
    def ifun():
        nonlocal index
        index = index + 1
        print("ifun",index,id(index))
        return index
    print("func2",index,id(index))
    return ifun

def make_test_dice(*outcomes):
    index = len(outcomes) - 1
    print("make_test_dice",index,id(index))
    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        print("dice",index,id(index))
        return outcomes[index]
    return dice
test_dice = make_test_dice(4,2,1)
# print(test_dice())
# print(test_dice())
# print(test_dice())
# print(type(test_dice))
# print(type(make_test_dice))
# print(type(make_test_dice(4,2,1)))
# print(test_dice is make_test_dice(4,2,1))
def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    def dice():
        return randint(1,sides)
    return dice
x = make_fair_dice(6)
print(x())
