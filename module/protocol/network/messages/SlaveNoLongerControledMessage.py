from module.protocol.network.message import Message


class SlaveNoLongerControledMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8594
        self.masterId = {"type": "Number", "value": ""}
        self.slaveId = {"type": "Number", "value": ""}
