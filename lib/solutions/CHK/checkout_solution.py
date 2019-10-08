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

        if item == "A":
            items[0] += 1
        elif item == "B":
            items[1] += 1
        elif item == "C":
            items[2] += 1
        elif item == "D":
            items[3] += 1
    print(items)
    items, offers = check_offers(items)

    total = sum([prices[item_key[i]] * items[i] for i in range(len(items))]) + offers

    print(int(total))
    return int(total)


def check_offers(items):

    offers = 0
    while items[0] > 3:
        offers += 130
        items[0] -= 3
    while items[1] > 2:
        offers += 45
        items[1] -= 2

    return items, offers


if __name__ == "__main__":
    checkout("AAAABBCCCCD")


