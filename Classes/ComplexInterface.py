import TestInterface


class ComplexInterface(TestInterface):
    model_sub_test_case = 0
    range_list = []  # 储存取值范围的list，和模板次级用例一一对应
    model_sub_test_case_list = []
    sub_test_case_list = [[]]

    def __init__(self):
        pass
