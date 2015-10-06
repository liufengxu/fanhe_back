#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2015 .com, Inc. All Rights Reserved
#
################################################################################
"""
description:
author: liufengxu
date: 2015-10-06 23:44:46
last modified: 2015-10-06 23:56:01
version:
"""

import logging
import sys


def leven_dist(str_a, str_b):
    len_a = len(str_a)
    len_b = len(str_b)
    edit = [([0] * len_a) for i in xrange(len_b)]
    edit[0][0] = 0
    for i in xrange(1, len_a):
        edit[0][i] = i
    for i in xrange(1, len_b):
        edit[i][0] = i
    for i in xrange(1, len_a):
        for j in xrange(1, len_b):
            if str_a[i] == str_b[j]:
                f = 0
            else:
                f = 1
            edit[i][j] = min(edit[i-1][j] + 1, edit[i][j-1] + 1,
                             edit[i-1][j-1] + f)
    return edit[len_a - 1][len_b - 1]


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    x = leven_dist(s1, s2)
    print x

if __name__ == '__main__':
    main()
