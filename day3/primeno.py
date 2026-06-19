def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    number = int(input("Enter a number to check if it is prime: "))
    if is_prime(number):
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")

    print("\nPrime numbers up to 20:")
    primes = [i for i in range(2, 21) if is_prime(i)]
    print(primes)


if __name__ == "__main__":
    main()
