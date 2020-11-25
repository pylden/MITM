from module.protocol.network.message import Message


class PrismFightJoinLeaveRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7685
        self.subAreaId = {"type": "uint", "value": ""}
        self.join = {"type": "Boolean", "value": ""}
