

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

    skus = list(skus)

    for sku in skus:
        if sku.isalpha() is False:
            return -1

    return int(total)



