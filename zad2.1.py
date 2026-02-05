import inspect

def log_params(func):
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs):
        bound = sig.bind_partial(*args, **kwargs)
        for name, value in bound.arguments.items():
            print(f"{name}: {type(value)}")
        return func(*args, **kwargs)

    return wrapper


@log_params
def demo(a, b, c="x", *, d=0):
    return a, b, c, d


if __name__ == "__main__":
    print("2.1 test:")
    print(demo(10, 3.5, d=True))
