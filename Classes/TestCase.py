class TestCase:
    interface_index_list = []  # 接口按顺序排列
    sub_case_list = []  # 储存子测试用例,和接口顺序一一对应
    total_coverage = 0  # 总覆盖率
    covered_branch = 1  # 用二进制序列表示分支覆盖率
    target_interface_index = 0  # 目标接口

    def __init__(self):
        pass



