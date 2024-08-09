from classes.Stack import Stack


def counter(n):

    print(n)
    if n == 1:
        return
    else:
        counter(n - 1)


def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():

    # counter(3)
    # print(factorial(5))

    stack = Stack()
    stack.push("daleale")
    stack.push("aledale")
    stack.push("alecupado")

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


main()
