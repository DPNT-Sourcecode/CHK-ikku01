from string import ascii_uppercase as asc_up

# noinspection PyUnusedLocal
# skus = unicode string

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50
}


def checkout(skus):

    items = [0] * 26
    item_key = list(asc_up)

    skus = list(skus)  # Split skus into individual units

    for sku in skus:

        try:  # Checks each value to make sure it is a valid entry
            item = prices[sku]
        except:
            return -1

        sku_pos = asc_up.index(sku)

        items[sku_pos] += 1

    items, offers = check_offers(items)
    # put each item through pricing scrutiny, then add on the pricing of the special offers
    total = sum([prices[item_key[i]] * items[i] for i in range(len(items))]) + offers

    print(total)
    return int(total)


def multibuy(items, items_on_offer):
    """Check if items in the particular order fulfil multibuy requirements to sub in an offer price
    for "buy any x items" offers.
    """
    offers = 0
    offer_items = []

    # pick interested items
    for i in range(len(items_on_offer)):
        j = asc_up.index(items_on_offer[i])
        for k in range(items[j]):
            offer_items.append((items_on_offer[i], prices[items_on_offer[i]]))

    print(offer_items)


    # sort items by price



    return items, offers


def check_offers(items):
    """Check for valid purchase amounts to trigger Special offer pricing and adjust accordingly.

    Adds the offer pricing into a special category and removes the items from standard pricing scrutiny.

    """

    offers = 0

    offer_set = ["S", "T", "X", "Y", "Z"]
    mb_items, o = multibuy([items[asc_up.index[k]] for k in offer_set], offer_set)
    offers += o

    e_items = int(items[asc_up.index("E")])  # 2E get one B free
    while e_items >= 2 and items[asc_up.index("B")] >= 1:
        items[asc_up.index("B")] -= 1
        e_items -= 2

    n_items = int(items[asc_up.index("N")])  # 3N get one M free
    while n_items >= 3 and items[asc_up.index("M")] >= 1:
        items[asc_up.index("M")] -= 1
        n_items -= 3

    r_items = int(items[asc_up.index("R")])  # 3R get one Q free
    while r_items >= 3 and items[asc_up.index("Q")] >= 1:
        items[asc_up.index("Q")] -= 1
        r_items -= 3

    while items[asc_up.index("A")] >= 5:  # 5A for 200
        offers += 200
        items[asc_up.index("A")] -= 5

    while items[asc_up.index("A")] >= 3:  # 3A for 130
        offers += 130
        items[asc_up.index("A")] -= 3

    while items[asc_up.index("B")] >= 2:  # 2B for 45
        offers += 45
        items[asc_up.index("B")] -= 2

    while items[asc_up.index("F")] >= 3:  # 2F get one F free
        offers += 20
        items[asc_up.index("F")] -= 3

    while items[asc_up.index("H")] >= 10:  # 10H for 80
        offers += 80
        items[asc_up.index("H")] -= 10

    while items[asc_up.index("H")] >= 5:  # 5H for 45
        offers += 45
        items[asc_up.index("H")] -= 5

    while items[asc_up.index("K")] >= 2:  # 2K for 150
        offers += 150
        items[asc_up.index("K")] -= 2

    while items[asc_up.index("P")] >= 5:  # 5P for 200
        offers += 200
        items[asc_up.index("P")] -= 5

    while items[asc_up.index("Q")] >= 3:  # 3Q for 80
        offers += 80
        items[asc_up.index("Q")] -= 3

    while items[asc_up.index("U")] >= 4:  # 3U get one U free
        offers += 120
        items[asc_up.index("U")] -= 4

    while items[asc_up.index("V")] >= 3:  # 3Q for 130
        offers += 130
        items[asc_up.index("V")] -= 3

    while items[asc_up.index("V")] >= 2:  # 2Q for 90
        offers += 90
        items[asc_up.index("V")] -= 2

    return items, offers


if __name__ == "__main__":
    checkout("QQSXYZZ")


