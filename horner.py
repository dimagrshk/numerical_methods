# try: from functools import reduce
# except: pass
#
# def horner(coeffs, x):
# 	return reduce(lambda acc, c: acc * x + c, reversed(coeffs), 0)
#
# print (horner( (1.158, -2.343, 0.572, 1.425, -1.217, 0.883), 0.5))

def horner(ls, x):
    res = 0
    print("row for " + str(x))
    for i in reversed(ls):
        res = round(res * x + i, 4)
        print(str(i) + " = " + str(res))
    print("\n")
    return res

ls_m = [1.158, -2.343, 0.573, 1.452, -1.217, 0.883]
ls_x_0 = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
print(ls_m)
for x_0 in ls_x_0:
    horner(ls_m, x_0)
