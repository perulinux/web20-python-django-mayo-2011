#!/usr/bin/env python
# -*- encoding: utf8 -*-

d1 = {
  'a': 10,
  'b': 20,
  'c': 30
}

print [v for v in d1.iterkeys()]
print [v for v in d1.itervalues()]
print [v for v in d1.iteritems()]

d1 = dict(d1.iteritems())
print d1
