import SubTestCase
import CoverageCalculater


class TestCase:
    interface_index_list = []  # 接口按顺序排列
    sub_case_list = []  # 储存子测试用例,和接口顺序一一对应
    total_coverage = 0  # 总覆盖率
    coverage = 0  # 用二进制序列表示分支覆盖率
    target_interface_index = None  # 目标接口

    def add_sub_test_case(self, sub_test_case):
        self.interface_index_list.appand(sub_test_case.index)
        self.sub_case_list.appand(sub_test_case)

    def __init__(self, sub_test_case, target_interface_index=None):
        self.add_sub_test_case(sub_test_case)
        self.target_interface_index = target_interface_index

    def terminal_test_case(self, coverage):
        self.total_coverage = CoverageCalculater.get_cover_percentage(coverage)
        self.coverage = coverage
