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
date: 2015-10-04 15:27:10
last modified: 2015-10-04 18:03:54
version:
"""

import logging
import re
import sys


def get_object(clean_file):
    with open(clean_file) as fp:
        for line in fp:
            segs = line[:-1].split('\t')
            if len(segs) != 7:
                logging.debug('Wrong format, %s segs found', len(segs))
                continue
            rid, name, score, done, pic, material, cate = segs
            idre = re.compile('/recipe/([0-9]+)/')
            if not idre.findall(rid):
                logging.debug('recipe id not found')
                continue
            id = idre.findall(rid)[0]
            m_list = []
            m_list.append(id)
            m_list.append(name)
            for m in material.split(','):
                m = m.split(':')[0]
                if m:
                    m_list.append(m)
            for c in cate.split(','):
                if c:
                    m_list.append(c)
            print '\t'.join(m_list)


def step_1(file_1):
    count = {}
    with open(file_1) as fp:
        for line in fp:
            segs = line[:-1].split('\t')
            # print '\n'.join(segs[1:])
            for i in segs:
                if i not in count:
                    count[i] = 0
                count[i] += 1
    for i in count:
        print i + '\t' + str(count[i])


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    # get_object(sys.argv[1])
    step_1(sys.argv[1])

if __name__ == '__main__':
    main()
