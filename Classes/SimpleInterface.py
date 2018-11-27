from Classes import TestInterface


class SimpleInterface(TestInterface.TestInterface):
    model_sub_test_case = 0
    sub_test_case_list = []

    def __init__(self, info, result, value_range):
        TestInterface.TestInterface.__init__(info, result)
        self.value_range = value_range



