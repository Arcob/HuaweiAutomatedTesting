from SimulationModulePackage import SortingMachine
from SimulationModulePackage import DataModelReader
from AlgorithmModulePackage import AlgorithmModule
from Classes import InterfaceRange


interface_list = None


def init():
    global interface_list
    interface_list = DataModelReader.read_data_module()
    print("SimulationModulePackage init")


def sort_and_send_span(treated_info):  # 输入处理后的请求（接口，输入等），返回一个接口,如果是复杂接口的话还返回输入对应的index
    result = interface_list[0]
    # 等待实现 根据treated_info发送相应接口和index信息给算法模块
    AlgorithmModule.receive_range_from_simulation_module(result)

