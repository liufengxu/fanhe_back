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
date: 2015-10-14 00:04:27
last modified: 2015-10-14 18:18:18
version:
"""

import logging
import os
import sys

import jieba
reload(sys)
sys.setdefaultencoding('utf8')


def jieba_cut(query):
    """ 使用结巴分词进行切词
        github: https://github.com/fxsjy/jieba
        """
    # 加载自定义词典
    if os.path.exists('recipe_dict.txt'):
        jieba.load_userdict('recipe_dict.txt')
    # 切分输入query，注意使用cut_for_search，获得更多切词结果
    seg_list = jieba.cut_for_search(query)
    return seg_list


def cut_all_line(input_file, index_file, dict_file):
    """ 整行进行切词建立正排索引
        其中第一列为标识id，否则容易出现错乱
        """
    term_dict = {}
    # ID初始值设定
    start_num = 1
    index_fp = open(index_file, 'w')
    dict_fp = open(dict_file, 'w')
    sys.stdout = index_fp
    with open(input_file) as fp:
        for line in fp:
            seg_list = jieba_cut(line[:-1])
            index_list = []
            for i in seg_list:
                if i not in term_dict:
                    term_dict[i] = start_num
                    start_num += 1
                index_list.append(str(term_dict[i]))
            # 保序去重，不可以用list，效率低
            nodup_list = list(set(index_list))
            nodup_list.sort(key=index_list.index)
            print ' '.join(nodup_list)
    sys.stdout = dict_fp
    for t in term_dict:
        print term_dict[t], t
    # 返回词典，为需要使用的情形备用
    return term_dict


def do_invert(forward_file, invert_file):
    """ 正排索引转倒排索引 """
    invert_fp = open(invert_file, 'w')
    sys.stdout = invert_fp
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


def kv_exchange(input_dict):
    """ 以词典的value做key重新构建词典 """
    return dict(zip(input_dict.values(), input_dict.keys()))


def human_view(index_file, id2term, human_file):
    human_fp = open(human_file, 'w')
    sys.stdout = human_fp
    with open(index_file) as fp:
        for line in fp:
            outlist = []
            segs = line[:-1].split(' ')
            for i in segs:
                num = int(i)
                if num in id2term:
                    outlist.append(id2term[num])
            print '\t'.join(outlist)


def main():
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    input_file = sys.argv[1]
    zheng_file = input_file + '.zheng'
    cidian_file = input_file + '.cidian'
    dao_file = input_file + '.dao'
    zheng_human = zheng_file + '.human'
    dao_human = dao_file + '.human'
    term2id = cut_all_line(input_file, zheng_file, cidian_file)
    do_invert(zheng_file, dao_file)
    human_read = False
    if human_read:
        id2term = kv_exchange(term2id)
        human_view(zheng_file, id2term, zheng_human)
        human_view(dao_file, id2term, dao_human)

if __name__ == '__main__':
    main()
