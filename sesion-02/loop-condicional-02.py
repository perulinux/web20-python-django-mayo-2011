#!/usr/bin/env python

i = 0
while i < 100:
    i += 1
    if i % 9 == 0 or i % 14 == 0:
        continue
    print i
