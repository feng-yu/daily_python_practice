"""
Test script to dump any thought in
"""


def par(*args, **kargs):
    for item in kargs.items():
        print(item)
    for k, v in kargs.items():
        print(k, v)


par(name='kate', age=38)