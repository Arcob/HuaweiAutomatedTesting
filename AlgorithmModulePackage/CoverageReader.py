import Logger
from Classes import CoverageInfo


def init():
    Logger.log("Combiner init")


def read_xml_info_into_coverage(info):  # info为读到的xml覆盖率信息,返回存好的coverage
    result = CoverageInfo.CoverageInfo(read_xml_into_dictionary(info))
    return result


def read_xml_into_dictionary(info):
    result = {}
    return result
