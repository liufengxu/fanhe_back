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
last modified: 2015-10-07 00:47:24
version:
"""

import logging
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def levenshtein_dist(list_a, list_b):
    len_a = len(list_a) + 1
    len_b = len(list_b) + 1
    edit = [([0] * len_b) for i in xrange(len_a)]
    edit[0][0] = 0
    for i in xrange(1, len_a):
        edit[i][0] = i
    for i in xrange(1, len_b):
        edit[0][i] = i
    for i in xrange(1, len_a):
        for j in xrange(1, len_b):
            if list_a[i - 1] == list_b[j - 1]:
                f = 0
            else:
                f = 1
            edit[i][j] = min(edit[i-1][j] + 1, edit[i][j-1] + 1,
                             edit[i-1][j-1] + f)
    for i in xrange(len_a):
        tmp_out = []
        for j in xrange(len_b):
            tmp_out.append(str(edit[i][j]))
        logging.debug('%s', ' '.join(tmp_out))
    return edit[len_a - 1][len_b - 1]


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    s1 = ['我', '是', '中', '国', '人']
    s2 = ['我', '国', '人', '口', '多']
    x = levenshtein_dist(s1, s2)
    print x

if __name__ == '__main__':
    main()
