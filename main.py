MENU_PROMPT = "Enter 'a' to print the nth term of the series, 'b' to print till the nth term of the series, 'q' to quit: "

selection = input(MENU_PROMPT)


def nth_number(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        a = 0
        b = 1
        sum = 0
        count = 1
        while (count <= n):
            count += 1
            a = b
            b = sum
            sum = a + b
        return sum


def till_number(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b


while selection != 'q':
    if selection == 'a':
        n = int(input('please enter n: '))
        print(nth_number(n))
    elif selection == 'b':
        n = int(input('please enter n: '))
        till_number(n)
