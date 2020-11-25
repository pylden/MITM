from module.protocol.network.message import Message


class PrismInfoJoinLeaveRequestMessage(Message):
    def __init__(self):
        self.id = 997
