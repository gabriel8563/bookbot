def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    characters_list = {}
    for character in text.lower():
        if character in characters_list:
            characters_list[character] += 1
        else:
            characters_list[character] = 1
    return characters_list

def sort_on(items):
    return items["num"]

def sort_dicts(char_dict):
    dicts_list = []
    for key, value in char_dict.items():
        if key.isalpha() == True:
            dicts_list.append({"char": key, "num": value})
    dicts_list.sort(reverse=True, key=sort_on)
    return dicts_list
