from Stack import Stack

def reverse_string(input_str):
    s = Stack()

    for i in range(len(input_str)):
        s.push(input_str[i])

    bin = ""
    while not s.is_empty():
        bin += s.pop()
        

    print(bin)
    return True


reverse_string("Sanchit")