bottles = 99


def bottlePlural(count: int):
    plural = f"{'' if bottles == 1 else 's'}"
    # 1 bottle, 99 bottles
    return f"{count} bottle{plural}"


def takeOneDown():
    global bottles
    bottles -= 1
    print("Take one down, pass it around!")


while bottles > 0:
    print(f"{bottlePlural(bottles)} of beer on the wall!")
    print(f"{bottlePlural(bottles)} of beer!")
    takeOneDown()
    print(f"{bottlePlural(bottles)} of beer on the wall!\n")
