from collections import defaultdict


# the hashmap is already implemented (don't worry about the hash function)
# so only I'm resolving a problem using dictionary

def is_anagram(word1, word2):
    arr_word = list(word1)

    for i in range(len(word2)):
        char = word2[i]
        if char in arr_word:
            remove_index = arr_word.index(char)
            del arr_word[remove_index]

    return len(arr_word) == 0


def is_repeat(word, words):
    for key in words.keys():
        if key != word and is_anagram(word, key):
            return True
    return False


def search_anagrams(arr):
    words = {}
    for word in arr:
        temp = []
        for other_word in arr:
            if is_anagram(word, other_word) and not is_repeat(word, words):
                temp.append(other_word)
        if len(temp) != 0:
            words[word] = temp

    return [val for val in words.values()]


def search_anagram_v2(arr):
    anagram_map = defaultdict(list)
    result = []

    for s in arr:
        sorted_s = tuple(sorted(s))
        anagram_map[sorted_s].append(s)

    for val in anagram_map.values():
        result.append(val)

    return result


def main():
    arr = ["key", "tea", "ran", "eat", "nar", "ate"]

    # print(search_anagrams(arr))
    print(search_anagram_v2(arr))


main()
