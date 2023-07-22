def print_greeting(name):
    print(f"Hello, {name}!")

def call_greeting(func, name):
    func(name)

call_greeting(print_greeting, "Python")
