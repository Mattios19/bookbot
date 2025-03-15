def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else: 
            char_count[char] = 1
    return char_count

def sort_characters_by_count(char_count):
    char_list = [{"char": char, "count": count} for char, count in char_count.items() if char.isalpha()]

    # Sort the list by count in descending order
    char_list.sort(key=lambda x: x["count"], reverse=True)

    return char_list