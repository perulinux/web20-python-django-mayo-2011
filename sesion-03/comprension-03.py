#!/usr/bin/env python
# -*- encoding: utf8 -*-

valores = (
  ('M', 'Masculino'),
  ('F', 'Femenino'),
)

print [t for t in valores]
print ["k: %s v: %s" % (k, v) for k,v in valores]
