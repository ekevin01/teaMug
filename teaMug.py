#The author's name is Ellen Kevin
class teaMug:
    """Represents a mug with tea in it."""
teamug=teaMug()
teamug.shape="round"
teamug.capacity="8 ounces"
teamug.amount=6   #amount of tea in the cup (in ounces)
teamug.color="blue"
teamug.material="ceramic"
def tea_drinking_simulation(seconds):
    tea_remaining=teamug.amount-(2*seconds)
    if seconds>=3:
        print("Tea mug is empty!")
    else:
        print(tea_remaining, "ounces of tea left in mug.")

tea_drinking_simulation(10)
tea_drinking_simulation(2)
