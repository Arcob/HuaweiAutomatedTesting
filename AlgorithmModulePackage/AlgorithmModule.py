from Classes import InterfaceRange
import Mutater
import Communicator

path_tree = []  # 储存路径的树
interface_dictionary = {}  #储存接口的字典结构


def init():
    print("AlgorithmModulePackage init")


def receive_range_from_simulation_module(range):
    interface_dictionary[range.index] = range
    sub_test_case = Mutater.get_sub_test_case_from_range(range)
    Communicator.send_mutated_sub_test_case(sub_test_case)  # 发送了第一个次级测试用例




