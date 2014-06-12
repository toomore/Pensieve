# -*- coding: utf-8 -*-
from collections import OrderedDict


data = {'apple': 4,
        'book': 3,
        'cat': 2,
        'duck': 1}

order_dict = OrderedDict(sorted(data.items(), key=lambda x: x[1]))

print order_dict
print sorted(data.items(), key=lambda x: x[1])
print order_dict['book']
