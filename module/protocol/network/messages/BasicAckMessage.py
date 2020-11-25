from module.protocol.network.message import Message


class BasicAckMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4378
        self.seq = {"type": "uint", "value": ""}
        self.lastPacketId = {"type": "uint", "value": ""}
