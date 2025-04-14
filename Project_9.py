# 9.1
def popular_words (text, words):
    text = text.lower()

    result_dict = {}
    result_dict = {word: text.count(word) for word in words}

    return result_dict

# 9.2
def difference(*args):
    if not args:
        return 0
    else:
        result = max(*args) - min(*args)
        result = round(result, 2)
        return result
