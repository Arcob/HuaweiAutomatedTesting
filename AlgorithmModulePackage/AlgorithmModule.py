from Classes import InterfaceRange
from Classes import TestCase
from Classes import PathTree
from AlgorithmModulePackage import Mutater
from AlgorithmModulePackage import CoverageReader
import Communicator
import Logger


path_tree = None  # 储存路径的树
interface_dictionary = {}  # 储存接口的字典结构 模拟模块发来接口编号和复杂接口代码后直接从这里面取
current_test_case = None  # 当前用例


def init():
    global path_tree
    path_tree = PathTree.PathTree()

    CoverageReader.init()
    Logger.log("AlgorithmModulePackage init")


def receive_range_from_simulation_module(interface, complex_interface_index=0):
    # interface_dictionary[range.index] = range
    sub_test_case = Mutater.get_sub_test_case_from_range(interface)
    global current_test_case
    if current_test_case is None:
        current_test_case = TestCase.TestCase(sub_test_case)
        Logger.log("Create new test case")
    else:
        current_test_case.add_sub_test_case(sub_test_case)
        Logger.log("Add new subTestCase to test case")

    Communicator.send_mutated_sub_test_case(sub_test_case)  # 发送了第一个次级测试用例


def receive_coverage(info):
    global current_test_case
    if current_test_case is None:
        Logger.error("Receive coverage when no test case exist")
    else:
        current_test_case.terminal_test_case(CoverageReader.read_xml_info_into_coverage(info))
        end_current_round()  # 结束本轮测试


def end_current_round():
    global current_test_case
    path_tree.add_test_case(current_test_case)
    current_test_case = None


