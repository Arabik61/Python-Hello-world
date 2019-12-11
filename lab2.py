dictionary = {'<': '&lt', '>': '&gt', '"': '&quot', '&': '&amp'}


def decorator(function):
    def wrapper(string):
        tag = function(string)
        new_tag = ""
        for x in tag:
            if x in dictionary.keys():
                new_tag += dictionary[x]
            else:
                new_tag += x
        return new_tag
    return wrapper


@decorator
def get_tag(tag):
    return tag


if __name__ == '__main__':
    tag = input("Your tag = ")
    print("Your escape tag: " + get_tag(tag))