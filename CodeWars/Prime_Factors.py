from math import * 

def prime_factors(n):
    d = 2
    factors = []
    factors_dict = {}
    result = ""

    while d <= sqrt(n):
        if n % d == 0:
            n /= d
            factors.append(d)
        else:
            d += 1

    factors.append(int(n))

    for i in range(len(factors)):
        factors_dict[factors[i]] = factors.count(factors[i])

    for x, y in factors_dict.items():
        if y > 1:
            result += f"({x}**{y})"
        else:
            result += f"({x})"

    return result

result = prime_factors(1)
print(result)