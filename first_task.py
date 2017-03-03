import math

def sln(A, a):
    d_a = A - a
    d_a_s = str(d_a)
    pos = d_a_s.find('.')
    right = d_a_s[pos + 1:]
    count = 1
    for cif in right:
        if cif == '0':
            count += 1
    mnog = 10 ** count
    tmp = d_a * mnog
    tmp = math.ceil(tmp)
    lim_d_a = tmp / mnog
    d_lim_a = lim_d_a / a

    return d_lim_a

a1 = 4.24
A1 = math.sqrt(18)
a2 = 0.818
A2 = 9/11.0
if sln(A1, a1) < sln(A2, a2):
    print("first")
else:
    print("second")