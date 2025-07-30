import os
import time
import random
import hashlib

def generate_seed():
    system_time = time.time()
    performance_counters = os.getpid() ^ os.getppid()
    random_noise = random.getrandbits(64)
    entropy_input = f"{system_time}-{performance_counters}-{random_noise}"
    seed_hash = hashlib.sha256(entropy_input.encode()).hexdigest()
    return seed_hash

# تجربة تشغيل
if __name__ == "__main__":
    seed = generate_seed()
    print("Seed:")
    print(seed)