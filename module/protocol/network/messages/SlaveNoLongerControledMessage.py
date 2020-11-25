from module.protocol.network.message import Message


class SlaveNoLongerControledMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8594
        self.masterId = {"type": "Number", "value": ""}
        self.slaveId = {"type": "Number", "value": ""}
