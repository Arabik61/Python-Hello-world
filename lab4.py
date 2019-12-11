def decorator(function):
    @wraps(function)
    def wrapper(string):
        input_string = function(string)
        return f"<body>{input_string}</body>"

    return wrapper


def wraps(function):
    def wrapper(dec_func):
        dec_func.__name__ = function.__name__
        dec_func.__doc__ = function.__doc__
        return dec_func
    return wrapper


@decorator
def get_tag(tag):
    """some text"""
    return tag


if __name__ == '__main__':
    print(get_tag.__name__)
    print(get_tag.__doc__)