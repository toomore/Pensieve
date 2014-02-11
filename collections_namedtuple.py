# -*- coding: utf-8 -*-
# http://docs.python.org/2/library/collections.html#collections.namedtuple
# https://github.com/kennethreitz/requests/blob/a5b3719967e685afe9e96359e69177fda0a10d44/requests/packages/urllib3/util.py#L269
from collections import namedtuple


People = namedtuple('People', ['name', 'age'])

people = People('toomore', 23)
print people

print people.name
print people.age

try:
    people.skill = 'python'
    print people.skill
except AttributeError as e:
    print e

people = people._replace(name='TOOMORE')
print people.name
print people._fields
print people._asdict()

# ----- Setting default people ----- #
default_people = People('<No body>', 18)
me_people = default_people._replace(name='me')
print me_people
