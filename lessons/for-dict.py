"""Practice with Dictionaries and for Loops"""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}

for key in in_stock:
        # key is "carrots" "beets" "apples"
        # in_stock[key] is values: True, False
        if in_stock[key]:
            # could also say if in_stock[key] is True: but dont have to
            print(key)