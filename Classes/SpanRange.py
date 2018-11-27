from Classes import Range
import MutateTool


class DictRange(Range.Range):  # 固定范围参数 只有一个值（一般为字符串）

    def __init__(self, min_value, max_value):
        self.min_value = min_value  # 最小值
        self.max_value = max_value  # 最大值

    def mutate_from_value(self, value, mutate_strategy=0):  # 如果突变策略在可处理之外就返回空值
        if mutate_strategy == MutateTool.MutateType.not_mutate:
            return value
        elif mutate_strategy == MutateTool.MutateType.empty_value_mutate:
            return MutateTool.empty_value_mutate(value)
        elif mutate_strategy == MutateTool.MutateType.add_one_mutate:
            return MutateTool.add_one_mutate_span(value, self.min_value, self.max_value)
        elif mutate_strategy == MutateTool.MutateType.minus_one_mutate:
            return MutateTool.minus_one_mutate_span(value, self.min_value, self.max_value)
        elif mutate_strategy == MutateTool.MutateType.max_value_mutate:
            return MutateTool.max_value_mutate_span(value, self.min_value, self.max_value)
        elif mutate_strategy == MutateTool.MutateType.min_value_mutate:
            return MutateTool.min_value_mutate_span(value, self.min_value, self.max_value)
        else:
            return ""

