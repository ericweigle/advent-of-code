#!/usr/bin/python3

import re
data = [x.strip() for x in open('input', 'r').readlines()]
ids = set([int(re.sub('[BR]', '1', re.sub('[FL]', '0', seat)), 2)
           for seat in data])
print(max(ids))
print([i for i in range(1000) if i not in ids and (i - 1) in ids and (i + 1) in ids])
