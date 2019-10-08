# noinspection PyUnusedLocal
# skus = unicode string

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}


def checkout(skus):

    items = [0, 0, 0, 0]
    item_key = ["A", "B", "C", "D"]

    skus = list(skus) # Split skus into individual units

    for sku in skus:

        try:  # Checks each value to make sure it is a valid entry
            item = prices[sku]
        except:
            return -1

        if sku == "A":
            items[0] += 1
        elif sku == "B":
            items[1] += 1
        elif sku == "C":
            items[2] += 1
        elif sku == "D":
            items[3] += 1

    items, offers = check_offers(items)

    # put each item through pricing scrutiny, then add on the pricing of the special offers
    total = sum([prices[item_key[i]] * items[i] for i in range(len(items))]) + offers

    return int(total)


def check_offers(items):
    """Check for valid purchase amounts to trigger Special offer pricing and adjust accordingly.

    Adds the offer pricing into a special category and removes the items from standard pricing scrutiny.

    >>> check_offers([4, 2, 4, 1])
    175
    >>> check_offers([2, 0, 5, 6])
    0
    """

    offers = 0
    while items[0] >= 3:
        offers += 130
        items[0] -= 3

    while items[1] >= 2:
        offers += 45
        items[1] -= 2

    return items, offers






