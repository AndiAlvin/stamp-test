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
    numbers = list(range(1, 101))
    numbers.reverse()

    for num in numbers:
        if is_prime(num):
            continue
        output = ""
        if num % 3 == 0:
            output += "Foo"
        if num % 5 == 0:
            output += "Bar"
        if output == "":
            output = num
        print(output, end=" ")

        if num % 10 == 1:
            print()  # Move to the next line after every 10 numbers

if __name__ == "__main__":
    main()
