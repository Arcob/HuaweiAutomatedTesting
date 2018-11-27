import CoverageCalculater


class CoverageInfo:

    def __init__(self, coverage_dictionary):
        self.coverage_dictionary = coverage_dictionary  # key为文件名，value为表示行覆盖率的二进制串

