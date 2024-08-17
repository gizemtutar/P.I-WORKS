# Asal sayı olup olmadığını kontrol eden fonksiyon
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 3 basamaklı ve 5 ile başlayan asal sayıları bulan fonksiyon
def find_primes_starting_with_5():
    primes = []
    for num in range(500, 600):
        if is_prime(num):
            primes.append(num)
    return primes

# Asal sayıları bul ve yazdır
primes = find_primes_starting_with_5()
print("Asal Sayılar:", primes)
