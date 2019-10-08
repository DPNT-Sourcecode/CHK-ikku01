

# noinspection PyUnusedLocal
# skus = unicode string

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}


def checkout(skus):
    total = 0
    items = [0, 0, 0, 0]

    skus = list(skus)

    for sku in skus:

        try:
            item = prices[sku]
        except KeyError():
            return -1

        if item == "A":
            items[0] += 1
        elif item == "B":
            items[1] += 1
        elif item ==  "C":
            items[2] += 1
        elif item == "D":
            items[3] += 1

    items, offers = check_offers(items)

    total = sum([prices[item] for item in items]) + offers

    return int(total)


def check_offers(items):

    

    return items, offers




