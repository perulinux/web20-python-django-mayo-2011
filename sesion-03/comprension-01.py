#!/usr/bin/env python
# -*- encoding: utf8 -*-

print range(10)
print [x for x in range(10)]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print [x+1 for x in range(10)]
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print [x*10 for x in range(10)]
#[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print [x*10 for x in range(10) if x % 2 == 0]
#[0, 20, 40, 60, 80]

