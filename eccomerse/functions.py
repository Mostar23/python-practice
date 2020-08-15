def times_table(x):
    for a in [1,2,3,4,5,6,7,8,9]:
        print(f"{x} x {a} = {x * a}")

def multiply(f):
    f(10)

multiply(times_table)

def takeout():
    n = input("Enter a word:")
    print(n)

    if n in "abdcdefghijklmnopqrstuvwxyz":
        print(n[1], n[2], n[3], n[4], n[5])

    return n[1], n[2], n[3],  n[4],  n[5]

print(takeout())


def takeout2():
    q = input("Enter a word: ")
    print(q)

    s = input("Enter how many letters you wanna see ?: ")
    print(s)

    if s in "2":
        print(q[0], q[1])

    if s in "3":
        print(q[0], q[1], q[2])

    if s in "4":
        print(q[0], q[1], q[2], q[3])

    if s in "skip 1" or "jump 1" and not ["1"]:
        print(q[0], q[2])

    if s in "5":
        print(q[0], q[1], q[2], q[3], q[4])

print(takeout2())


def facctorial():
    o = int(input("Enter a number to get the factorial: "))
    print(o)

    if o in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
        if o == 9:
            print("9!")
            print(9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)

        elif o == 8:
            print("8!")
            print(8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)

        elif o == 7:
            print("7!")
            print(7 * 6 * 5 * 4 * 3 * 2 * 1)

        elif o == 6:
            print("6!")
            print(6 * 5 * 4 * 3 * 2 * 1)

        elif o == 5:
            print("5!")
            print(5 * 4 * 3 * 2 * 1)

        elif o == 4:
            print("4!")
            print(4 * 3 * 2 * 1)

        elif o == 3:
            print("3!")
            print(3 * 2 * 1)


        elif o == 2:
            print(2 * 1)

    return o



print(facctorial())


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Input a number to compute the factiorial : "))
print(factorial(n))











































































        















