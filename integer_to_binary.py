from Stack import Stack

def divide_by_2(num):
    s = Stack()
    while num > 0:
        remainder = num % 2
        s.push(remainder)
        num = num // 2

    binary = ""
    while not s.is_empty():
        binary += str(s.pop())

    print(binary)
    return binary

divide_by_2(669)