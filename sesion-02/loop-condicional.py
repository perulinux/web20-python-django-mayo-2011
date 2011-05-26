#!/usr/bin/env python

i = 1
while i <= 100:
    if i % 9 == 0 or i % 14 == 0:
        i += 1
        continue
    print i
    i += 1
