import random

from dual import Dual


def blackboxfun(i):
    return Dual(4) + Dual(3) * i - Dual(2) * i*i + i*i*i

# NTE : coefficients need to be dual to work !!!!!!



found = False
r = random.randint(0, 100)

while not found:
    print(r)
    rr = blackboxfun(Dual(r))
    if rr.derivative > 0:
        if r == 100:
            raise RuntimeError("nomin right side")
        r = random.randint(r, 100)
    elif rr.derivative < 0:
        if r == 0:
            raise RuntimeError("nomin left side")
        r = random.randint(0, r)
    else: ## ==0  !! it is a local extremum
        print(f"minimum found : bbf({r}) = {rr}")
        found = True








