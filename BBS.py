import math
from seed_generator import generate_seed  # استدعاء من ملفك المرفوع

# إنشاء N من p و q
def generate_modulus(p, q):
    if p % 4 != 3 or q % 4 != 3:
        raise ValueError("p and q must be ≡ 3 mod 4")
    return p * q

# خوارزمية BBS
def bbs(seed, n, bit_count):
    x = seed
    bits = []
    for _ in range(bit_count):
        x = pow(x, 2, n)
        bits.append(x % 2)
    return bits

# تجربة تشغيل
if __name__ == "__main__":
    p = 11
    q = 19
    n = generate_modulus(p, q)

    seed = generate_seed(n)  # توليد seed من الكود اللي رفعته
    print("Seed:", seed)

    bits = bbs(seed, n, 20)
    print("Generated bits:", ''.join(map(str, bits)))
