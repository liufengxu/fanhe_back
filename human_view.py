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
date: 2015-09-21 15:40:35
last modified: 2015-09-21 16:26:58
version:
"""

import logging
import sys


def build_id_tag_dict(tag_table):
    id_tag = {}
    with open(tag_table) as fp:
        for line in fp:
            id, name = line[:-1].split('\t')
            id_tag[id] = name
    return id_tag


def show_tag(input_file, tag_table):
    id_tag = build_id_tag_dict(tag_table)
    with open(input_file) as fp:
        for line in fp:
            out_list = []
            for id in line[:-1].split():
                if id in id_tag:
                    out_list.append(id_tag[id])
                else:
                    logging.debug('id: %s not found', id)
            print '\t'.join(out_list)


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    input_file = sys.argv[1]
    tag_table = sys.argv[2]
    show_tag(input_file, tag_table)

if __name__ == '__main__':
    main()
