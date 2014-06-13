# -*- coding: utf-8 -*-
from collections import OrderedDict


data = {'apple': 4,
        'book': 3,
        'cat': 2,
        'duck': 1}

order_dict = OrderedDict(sorted(data.items(), key=lambda x: x[1]))

print order_dict
sorted_list = sorted(data.items(), key=lambda x: x[1])

print sorted_list
for i in sorted_list:
    print i

print order_dict['book']
