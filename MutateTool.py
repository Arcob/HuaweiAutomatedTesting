from enum import Enum
import Logger


class MutateType(Enum.IntEnum):
    not_mutate = 1
    empty_value_mutate = 2
    add_one_mutate = 3
    minus_one_mutate = 4
    max_value_mutate = 5
    min_value_span = 6


def empty_value_mutate(value):
    return ""


def add_one_mutate_dict(value, value_range):  # 字典类型用的
    if value not in value_range:
        Logger.error("value not in range when neighbor_value_mutate for dict range")
        return ""
    index = value_range.index(value)
    if index == (len(value_range) - 1):
        add_one_index = 0
    else:
        add_one_index = index+1
    return value_range[add_one_index]


def minus_one_mutate_dict(value, value_range):  # 字典类型用的
    if value not in value_range:
        Logger.error("value not in range when neighbor_value_mutate for dict range")
        return ""
    index = value_range.index(value)
    if index == 0:
        minus_one_index = (len(value_range) - 1)
    else:
        minus_one_index = index-1
    return value_range[minus_one_index]


def add_one_mutate_span(value, min_value, max_value):  # 范围类型用的
    if value < min_value | value > max_value:
        Logger.error("value not in range when neighbor_value_mutate for span range")
        return ""
    if value == max_value:
        add_one_value = min_value
    else:
        add_one_value = value+1
    return add_one_value


def minus_one_mutate_span(value, min_value, max_value):  # 范围类型用的
    if value < min_value | value > max_value:
        Logger.error("value not in range when neighbor_value_mutate for span range")
        return ""
    if value == min_value:
        minus_one_value = max_value
    else:
        minus_one_value = value-1
    return minus_one_value


def max_value_mutate_dict(value, value_range):
    if value not in value_range:
        Logger.error("value not in range when max_value_mutate_dict for dict range")
        return ""
    return value_range[len(value_range)-1]


def min_value_mutate_dict(value, value_range):
    if value not in value_range:
        Logger.error("value not in range when min_value_mutate_dict for dict range")
        return ""
    return value_range[0]


def max_value_mutate_span(value, min_value, max_value):
    if value < min_value | value > max_value:
        Logger.error("value not in range when max_value_mutate_span for span range")
        return ""
    return max_value


def min_value_mutate_span(value, min_value, max_value):
    if value < min_value | value > max_value:
        Logger.error("value not in range when min_value_mutate_span for span range")
        return ""
    return min_value
