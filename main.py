print('Enter Five Numbers')
while True:
    try:
        a = int(input())
        b = int(input())
        c = int(input())
        d = int(input())
        e = int(input())
        user_numbers = [a, b, c, d, e]
        break
    except ValueError:
        print("kindly Enter an Integer")
        continue
print(sorted(user_numbers))
