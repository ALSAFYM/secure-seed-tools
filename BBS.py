from seed_generator import generate_seed

def bbs(seed, n, bit_count):
    x = seed
    bits = []
    for _ in range(bit_count):
        x = pow(x, 2, n)
        bits.append(x % 2)
    return bits

if __name__ == "__main__":
    p = 499
    q = 547
    n = p * q

    seed_hash = generate_seed()
    seed_int = int(seed_hash, 16)

    bits = bbs(seed_int, n, 32)

    print("Seed (hex):", seed_hash)
    print("Seed (int):", seed_int)
    print("Random bits:", ''.join(map(str, bits)))
