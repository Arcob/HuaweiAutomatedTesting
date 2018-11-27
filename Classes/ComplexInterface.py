from Classes import TestInterface


class ComplexInterface(TestInterface.TestInterface):
    model_sub_test_case_list = []
    sub_test_case_list = []  # 储存sub_test_case的list，每个list和value一一对应

    def __init__(self, info, result, value_range_list):
        TestInterface.TestInterface.__init__(info, result)
        self.value_range_list = value_range_list  # 储存取值范围的list，和模板次级用例一一对应

