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
date: 2015-10-07 22:03:15
last modified: 2015-10-08 23:56:49
version:
"""

import logging
import sys
import os

import jieba


def jieba_cut(query):
    # 加载自定义词典
    if os.path.exists('recipe_dict.txt'):
        jieba.load_userdict('recipe_dict.txt')
    # 切分输入query，切分结果为生成器
    seg_gen = jieba.cut(query)
    result_list = []
    for i in seg_gen:
        result_list.append(i)
    return result_list


def term2id(term_list):
    term_table = {}
    with open('r.id.tbl') as fp:
        for line in fp:
            segs = line[:-1].split('\t')
            if len(segs) != 2:
                logging.debug('Id table format not write')
                continue
            id, term = segs
            term_table[term] = id
    logging.debug('here')
    id_list = []
    for term in term_list:
        logging.debug('term is %s', term)
        if term in term_table:
            id_list.append(term_table[term])
    return id_list

def main():
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    query = sys.argv[1]
    seg_list = jieba_cut(query)
    print ' '.join(seg_list)
    id_list = term2id(seg_list)
    print ' '.join(id_list)

if __name__ == '__main__':
    main()
