import random
import typing

from dual import Dual


def blackboxfun(i):
    return Dual(4) + Dual(3) * i + Dual(42) * i*i - i*i*i

# NOTE : coefficients need to be dual to work !!!!!!
# => cannot be used as is on existing code
# => could be used as imlpementation of new language,
# where constants are implicit duals (or more, see grassman - n dimensions)
# Benefit: Transparent Automatic optimization of simple systems :
#   -

def draw(m, M):
    return (m + M) // 2


def find_min(m, M) -> bool:
    if M - m == 1:
        print(f"Minimum in {m} {M}")
        return True

    r = draw(m, M)
    rr = blackboxfun(Dual(r))
    print(f"{r} -> {rr.real} {rr.derivative}")
    if rr.derivative > 0:
        if r == m:
            raise RuntimeError("nomin left side")
        return find_min(m, r)
    elif rr.derivative < 0:
        if r == M:
            raise RuntimeError("nomin right side")
        return find_min(r, M)
    else: ## ==0  !! it is a local extremum
        print(f"minimum found : bbf({r}) = {rr}")
        return True


find_min(-100, 100)





