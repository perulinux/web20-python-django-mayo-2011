#!/usr/bin/env python

for i in range(1, 100 + 1):
    if i % 9 == 0 or i % 14 == 0:
        continue
    print i
