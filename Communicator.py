import Logger
from AlgorithmModulePackage import AlgorithmModule
from SimulationModulePackage import SimulationModule


def init():
    print("Communicator init")


def on_receive_test_request(info):
    treated_info = 0
    # treatedInfo = treat(info)
    SimulationModule.sort_and_send_span(treated_info)


def on_receive_coverage_information(info):
    AlgorithmModule.receive_coverage(read_into_coverage(info))


def send_mutated_sub_test_case(testCase):  # 发送次级测试用例后等待华为那边发回下一次测试请求（另一个接口）
    pass


def listen(info):
    if info == 1:
        on_receive_coverage_information(info)
    elif info == 2:
        on_receive_test_request(info)


def read_into_coverage(info):  # 将传来的覆盖率信息（xml）读为coverage
    result = 0
    return result

