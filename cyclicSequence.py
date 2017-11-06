def cyclicSequence(s):
    cyc = 0
    p = s[0]
    for c in sequence[1:]:
        if c <= p:
            if not cyc:
                cyc = 1
            else:
                return False
        p = c

    if cyc:
        return sequence[0] > sequence[-1]
    return True

a = -10
b = -3
print(a // b)
