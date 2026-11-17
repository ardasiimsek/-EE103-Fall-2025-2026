# Tuples: Functions with variable number of arguments


def mean(*args):
    # args is a TUPLE of all the arguments: mean(4, 6, 8) -> args = (4, 6, 8)
    # import pdb; pdb.set_trace()   # breakpoint: try  p type(args)  and  p args
    tot = 0
    for arg in args:
        # mean(1, 2, '3', 4, 5) used to fail here with
        # TypeError: unsupported operand type(s) for +=: 'int' and 'str'
        # so every argument is converted to float first
        tot += float(arg)
    return tot / len(args)


print(mean(4, 6, 8))            # 6.0
print(mean(1, 2, 3, 4, 5))      # 3.0
print(mean(1, 2, '3', 4, 5))    # 3.0 (works after the fix)

# One-element tuples
dummy1 = (3)
dummy2 = (3,)
print(type(dummy1))   # <class 'int'>   -> parentheses alone are just grouping
print(type(dummy2))   # <class 'tuple'> -> the comma makes it a tuple
