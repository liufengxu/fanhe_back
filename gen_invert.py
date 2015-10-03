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
date: 2015-09-21 15:54:55
last modified: 2015-09-21 16:29:05
version:
"""

import logging
import sys


def do_invert(forward_file):
    inv_dict = {}
    with open(forward_file) as fp:
        for line in fp:
            segs = line[:-1].split()
            for tag in segs[1:]:
                if tag not in inv_dict:
                    inv_dict[tag] = []
                inv_dict[tag].append(segs[0])
    for tag in inv_dict:
        print tag, ' '.join(inv_dict[tag])


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    forward_file = sys.argv[1]
    do_invert(forward_file)

if __name__ == '__main__':
    main()
