dictionary = {'<': '&lt', '>': '&gt', '"': '&quot', '&': '&amp'}


def escape_html(function):
    def wrapper(string):
        tag = function(string)

        new_tag = [dictionary[char] if char in dictionary.keys() else char for char in tag]

        return ''.join(new_tag)

    return wrapper


@escape_html
def get_tag(tag):
    return tag


if __name__ == '__main__':
    tag = input("Your tag = ")
    print("Your escape tag: " + get_tag(tag))
