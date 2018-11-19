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
    pass


def send_mutated_test_case(testCase):
    pass


def listen(info):
    if info == 1:
        on_receive_coverage_information(info)
    elif info == 2:
        on_receive_test_request(info)
