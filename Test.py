import Communicator
from Classes import SubTestCase


def start():
    Communicator.on_receive_test_request(0)


def give_fake_sub_test_case():
    return SubTestCase(info="aaa", result="bbb", value="ccc")
