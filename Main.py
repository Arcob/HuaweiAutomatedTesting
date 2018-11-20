#!/usr/bin/python
# -*- coding: UTF-8 -*-

from AlgorithmModulePackage import AlgorithmModule
from SimulationModulePackage import SimulationModule
import Logger
import Communicator
import CoverageCalculater
import Test

system_running = True  # 系统在运行
test_running = True  # 整体测试在运行（外层loop）
round_running = True  # 当前一轮测试在运行（内层loop）

# 初始化
Logger.log("初始化算法模块")
AlgorithmModule.init()
Logger.log("初始化模拟模块")
SimulationModule.init()
Logger.log("初始化通讯器")
Communicator.init()

a = 0b1110110000
b = 131231231231232
print(CoverageCalculater.number_of_1(a))
print(CoverageCalculater.get_cover_percentage(b))
# while (system_running):
#    Communicator.listen()


