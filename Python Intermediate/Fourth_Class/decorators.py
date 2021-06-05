#  Single wrapper syntax and logic

def rule_or_logic_to_apply(func):
    def wrapper():
        # your logic here
        func()  # executes the wrapped function
        return wrapper
    return func


@rule_or_logic_to_apply
def function_to_be_wrapped():
    pass

