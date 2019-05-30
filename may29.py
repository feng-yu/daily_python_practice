"""
Implement an autocomplete system.
That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""


def query_substr(substr, strlist):
    return filter(lambda x: x.startswith(substr), strlist)


s = 'de'
l = ['dog', 'deer', 'deal']
print(set(query_substr(s, l)))

