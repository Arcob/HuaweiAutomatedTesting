from Classes import Range


class TestInterface:
    index = 0  # 接口编号

    def __init__(self, info, result):
        self.info = info  # 不需要突变的info
        self.result = result  # result传过来一个list，存[true, false]或[true]或[false]

