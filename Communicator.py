import Logger
from AlgorithmModulePackage import AlgorithmModule
from SimulationModulePackage import SimulationModule


def init():
    print("Communicator init")


def on_receive_test_request(info):
    SimulationModule.sort_and_send_span(treat_test_request(info))  # 将处理过的测试请求发送给模拟模块


def on_receive_coverage_information(info):  # info为表示覆盖率的xml信息
    AlgorithmModule.receive_coverage(info)


def send_mutated_sub_test_case(testCase):  # 发送次级测试用例后等待华为那边发回下一次测试请求（另一个接口）
    pass


def listen(info):
    if info == 1:
        on_receive_coverage_information(info)
    elif info == 2:
        on_receive_test_request(info)


def treat_test_request(info):
    # 这里写解析测试请求的方法，将测试请求解析成模拟模块可读的格式后返回
    treated_info = 0
    return treated_info
