def bijectiveNumeration(n, domain):
    thingIndex = (n-1) / 99
    digit = n % 99


    index = int(thingIndex % len(domain)) # prevent out of range
    thing = domain[index]
    return "{}-{:02}".format(thing, digit)



print (bijectiveNumeration(134, ["MONKEYS", "PENGUINS", "ZEBRAS", "LIONS"]) , "vs PENGUINS-35")
print (bijectiveNumeration(1, ["MONKEYS", "PENGUINS", "ZEBRAS", "LIONS"]), "vs MONKEYS-01")
print (bijectiveNumeration(99, ["MONKEYS", "PENGUINS", "ZEBRAS", "LIONS"]), "vs MONKEYS-99")
print (bijectiveNumeration(100, ["MONKEYS", "PENGUINS", "ZEBRAS", "LIONS"]), "vs PENGUINS-01")

