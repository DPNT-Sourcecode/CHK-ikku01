
# noinspection PyUnusedLocal
# skus = unicode string

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10
}


def checkout(skus):

    items = [0] * 26
    item_key = ["A", "B", "C", "D", "E", "F"]

    skus = list(skus)  # Split skus into individual units

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
        elif sku == "E":
            items[4] += 1
        elif sku == "F":
            items[5] += 1

    items, offers = check_offers(items)
    # put each item through pricing scrutiny, then add on the pricing of the special offers
    total = sum([prices[item_key[i]] * items[i] for i in range(len(items))]) + offers

    return int(total)


def check_offers(items):
    """Check for valid purchase amounts to trigger Special offer pricing and adjust accordingly.

    Adds the offer pricing into a special category and removes the items from standard pricing scrutiny.

    >>> check_offers([4, 2, 4, 1, 0, 0])
    175
    >>> check_offers([4, 2, 4, 1, 4, 0])
    130
    >>> check_offers([2, 0, 5, 6, 0, 0])
    0
    >>> check_offers([2, 3, 5, 6, 2, 3])
    65
    """

    offers = 0

    while items[0] >= 5:  # 5A for 200
        offers += 200
        items[0] -= 5

    while items[0] >= 3:  # 3A for 130
        offers += 130
        items[0] -= 3

    e_items = int(items[4])  # 2E get one B free
    while e_items >= 2 and items[1] >= 1:
        items[1] -= 1
        e_items -= 2

    while items[1] >= 2:  # 2B for 45
        offers += 45
        items[1] -= 2

    while items[5] >= 3:  # 2F get one F free
        offers += 20
        items[5] -= 3

    return items, offers





