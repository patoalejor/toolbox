import itertools


# Option one: 
# Group in a dictionary if there are elements that need to appear only once in the pool
dict_1 = {'item 1': True, 'item 2': False}
dict_2 = {'item 3': 1, 'item 4': 3.1416}
dict_3 = {'item 5': 'hello', 'item 6': [1 ,2 ,3]}

all_combo = [dict_1, dict_2, dict_3]
_pool = itertools.product(*all_combo)
_pool = [list(combo) for combo in list(_pool)]

for p in _pool:
  print(p)


# Option two:
# Make each individual element in the pool part of the list
# variables with only one item are repeated always eg. items 5, 6
item_1 = [True, False]
item_2 = [1 , 0]
item_3 = [0.001, 0.999]
item_4 = ['hello', 'world']
item_5 = [None]
item_6 = [' ']

all_combo = [item_1, item_2, item_3, item_4, item_5, item_6]
_pool = itertools.product(*all_combo)
_pool = [list(combo) for combo in list(_pool)]

for p in _pool:
  print(p)