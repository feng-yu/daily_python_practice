"""
[medium]
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""
import functools


@functools.lru_cache(maxsize=1000)
def way_decode_one_two_only(code):
    """using recursive to calculate the ways for code that only container 1 or 2"""
    if code == '' or len(code) == 1:
        return 1
    else:
        return way_decode_one_two_only(code[1:]) + way_decode_one_two_only(code[2:])


def way_decode(code):
    #dictionary is not used in the method, just give a clear picture
    dictionary = {1:'a', 2:'b', 3:'c',4:'d', 5:'e', 6:'f', 7:'g', 8:'h',
           9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p',
           17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

    #to split the code into some lists that only contains 1 or 2.
    special_codes = ['10', '20', '13', '23', '14', '24', '15', '25', '16', '26', '17', '18', '19']
    code_list = [code]
    for special_code in special_codes:
        tem_list = []
        for index in range(len(code_list)):
            tem_list += code_list[index].split(special_code)
        code_list = tem_list

    n = 1
    for code in code_list:
        n = n * way_decode_one_two_only(code)

    return n


# test_code = '111'    #answer is 3
test_code = '10231111712'   #answer is 6
print(way_decode(test_code))
