def add_tag(tag):
    def decorator(function):
        def wrapper(string):
            input_string = function(string)
            return f"<{tag}>{input_string}</{tag}>"

        return wrapper

    return decorator


@add_tag("body")
def get_tag(tag):
    return tag


if __name__ == '__main__':
    tag = input("Your string = ")
    print("Your tag: " + get_tag(tag))