import TestCase


class PathTree:
    path_tree = []
    test_case_list = []  # 每个储存单元储存一个test_case列表

    def __init__(self):
        pass

    def exist_path(self, interface_index_list):
        for path in self.path_tree:
            if path == interface_index_list:
                return True
        return False

    def add_test_case(self, test_case):
        if test_case.interface_index_list in self.path_tree:
            temp_list = self.test_case_list[self.path_tree.index(test_case.interface_index_list)]
            temp_list.append(test_case)
            temp_list.sort()  # 补充排序方法
        else:
            self.path_tree.append(test_case.interface_index_list)
            self.test_case_list.append([test_case])

    def scan_for_first(self):  # 查找下一个
        #  之后再实现
        return self.path_tree[0]



