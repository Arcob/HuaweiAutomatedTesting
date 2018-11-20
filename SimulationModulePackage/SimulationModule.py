from SimulationModulePackage import SortingMachine
from SimulationModulePackage import DataModelReader
from AlgorithmModulePackage import AlgorithmModule
from Classes import InterfaceRange


def init():
    DataModelReader.read_data_module()
    print("SimulationModulePackage init")


def sort_and_send_span(info):
    AlgorithmModule.receive_range_from_simulation_module(InterfaceRange(1))

