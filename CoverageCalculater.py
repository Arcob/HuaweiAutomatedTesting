#!/usr/bin/python
# -*- coding: UTF-8 -*-

total_length = 0


def read_into_coverage(coverage_file):
    pass
    return 1


def get_intersection(coverage1, coverage2):  # 求交集
    result = coverage1 & coverage2
    return result


def get_union(coverage1, coverage2):  # 求并集
    result = coverage1 | coverage2
    return result


def get_difference(coverage1, coverage2):  # 求差集,前面减去后面
    result = coverage1 & (~coverage2)
    return result


def get_coverage_of_branch(coverage, index):  # 判断第index个branch是否被覆盖，branch数从第0位开始
    result = False if ((coverage & (1 << (index-1))) == 0) else True
    return result


def number_of_1(coverage):  # 判断有几个1
    count = 0
    while coverage > 0:
        count += 1
        coverage = (coverage-1) & coverage
    return count


def get_branch_num(coverage):
    return coverage.bit_length()


def get_cover_percentage(coverage):  # 返回覆盖率百分比
    return number_of_1(coverage)/(total_length if total_length != 0 else get_branch_num(coverage))
