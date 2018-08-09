# -*- coding: utf-8 -*-

import hashlib

filename = "01a436f4bd504666b2f6361c26f5efe1.kgtemp"
with open(filename, 'rb') as f:
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    print(hash)