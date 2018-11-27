from Classes import Range
import MutateTool


class FixedRange(Range.Range):  # 固定范围参数 只有一个值（一般为字符串）

    def __init__(self, value):
        self.value = value

    def mutate_from_value(self, value, mutate_strategy=0):  # 如果突变策略在可处理之外就返回空值
        if mutate_strategy == MutateTool.MutateType.not_mutate:
            return value
        elif mutate_strategy == MutateTool.MutateType.empty_value_mutate:
            return MutateTool.empty_value_mutate(value)
        else:
            return ""


