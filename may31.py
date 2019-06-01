"""
[hard]
Given an integer k and a string s,
find the length of the longest substring that contains at most k distinct characters.

For example,
given s = "abcba" and k = 2,
the longest substring with k distinct characters is "bcb".
"""


def find_adjacent_distinct_characters(k, s):
    """
    find the string and length of adjacent disstenct characters starting with first character in s
    :param k: distinct character count
    :param s: string
    :return: the length of the string and string itself.
    """
    if len(s) > k:
        characters = {s[0]:1}
        distinct_characters_count = 1
        for character in s[1:]:
            if distinct_characters_count < k:
                if character in characters:
                    characters[character] += 1
                else:
                    characters[character] = 1
                distinct_characters_count = len(characters)
            elif distinct_characters_count == k:
                if character in characters:
                    characters[character] += 1
                else:
                    break
            else:
                break
        total_characters_count = 0
        for _, count in characters.items():
            total_characters_count += count
        return total_characters_count, s[:total_characters_count]
    else:
        return len(s), s


def max_adjacent_distinct_character(k, s):
    max_count, max_string = find_adjacent_distinct_characters(k, s)
    for i in range(1, len(s)-k):
        count, string = find_adjacent_distinct_characters(k, s[i:])
        if count > max_count:
            max_count = count
            max_string = string
    return max_count, max_string

def main():
    s = 'abcba'
    k = 2
    print(max_adjacent_distinct_character(k, s))

main()
