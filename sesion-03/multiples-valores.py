#!/usr/bin/env python
# -*- encoding: utf8 -*-

def un_num_antes_y_despues(num):
    if num > 0:
        return (num - 1, num, num + 1, )
    else:
	return None

a, b, c = un_num_antes_y_despues(10)

print "a: %d b: %d c: %d" % (a, b, c)
