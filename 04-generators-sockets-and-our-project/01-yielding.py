def get_primes_by_yielding(max_value):
    for maybe_prime in range(2, max_value, 1):
        is_prime = True
        for x in range(maybe_prime):
            if x > 1 and maybe_prime % x == 0:
                is_prime = False
                break
        if is_prime:
            yield maybe_prime

def get_primes_up_to(max_value):
    all_primes = []
    for maybe_prime in range (2, max_value, 1):
        is_prime = True
        for x in range(maybe_prime):
            if x > 1 and maybe_prime % x == 0:
                is_prime = False
                break
            if is_prime:
                all_primes.append(maybe_prime)
    return all_primes


print( get_primes_by_yielding(100000) )

for x in get_primes_by_yielding(100000):
    print(x)

print(get_primes_up_to(100000))
