from Classes import TestInterface


class SimpleInterface(TestInterface.TestInterface):
    model_sub_test_case = 0
    range = 0

    def __init__(self):
        TestInterface.TestInterface.__init__(self)


