STACK = []
TOP = None

def is_empty():
    if len(STACK) == 0:
        return True

    return False

def push(item):
    global TOP
    STACK.append(item)

    TOP = len(STACK) - 1

def peek():
    if is_empty():
        return None
    return STACK[TOP]

def pop():
    global TOP
    if is_empty():
        return "Stack Underflow"

    popped = STACK.pop()
    TOP = len(STACK) - 1

    if TOP == 0:
        TOP = None

    return popped

def display():
    if is_empty():
        print("Stack is empty.")
        return

    for item in STACK[::-1]:
        print(item)