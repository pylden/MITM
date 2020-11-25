from module.protocol.network.message import Message


class PrismInfoJoinLeaveRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 997
        self.join = {"type": "Boolean", "value": ""}
