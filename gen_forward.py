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
date: 2015-09-19 20:49:28
last modified: 2015-09-21 15:56:16
version:
"""

import logging
import sys


def build_tag_id_dict(tag_table):
    tag_id = {}
    with open(tag_table) as fp:
        for line in fp:
            id, name = line[:-1].split('\t')
            tag_id[name] = id
    return tag_id


def paste_tag(input_file, tag_table):
    tag_id = build_tag_id_dict(tag_table)
    with open(input_file) as fp:
        for line in fp:
            segs = line[:-1].split('\t')
            rid = segs[0]
            fid = segs[-2]
            tid = segs[-1]
            tag_list = []
            for item in fid.split(','):
                if item:
                    if len(item.split(':', 1)) != 2:
                        break
                    f_name, f_unit = item.rsplit(':', 1)
                    if f_name in tag_id:
                        tag_list.append(tag_id[f_name])
            for item in tid.split(','):
                if item in tag_id:
                    tag_list.append(tag_id[item])
            print rid, ' '.join(tag_list)


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    input_file = sys.argv[1]
    tag_table = sys.argv[2]
    paste_tag(input_file, tag_table)

if __name__ == '__main__':
    main()
