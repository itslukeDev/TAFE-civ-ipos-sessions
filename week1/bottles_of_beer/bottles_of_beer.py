def bottle_plural(count: int) -> str:
    plural = "" if count == 1 else "s"
    return f"{count} bottle{plural}"


def take_one_down(bottles: int) -> int:
    bottles -= 1
    print("Take one down, pass it around!")
    return bottles


def sing_song(bottles: int):
    while bottles > 0:
        print(f"{bottle_plural(bottles)} of beer on the wall!")
        print(f"{bottle_plural(bottles)} of beer!")
        bottles = take_one_down(bottles)
        print(f"{bottle_plural(bottles)} of beer on the wall!\n")


# Start the song with 99 bottles
sing_song(99)
