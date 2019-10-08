import sys

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

    skus = list(skus)

    for sku in skus:

        try:
            item = prices[sku]
        except KeyError():
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

    total = sum([prices[item_key[i]] * items[i] for i in range(len(items))]) + offers

    return int(total)


def check_offers(items):

    offers = 0
    while items[0] >= 3:
        offers += 130
        items[0] -= 3

    while items[1] >= 2:
        offers += 45
        items[1] -= 2

    return items, offers



