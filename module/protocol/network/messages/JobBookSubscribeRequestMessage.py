from module.protocol.network.message import Message


class JobBookSubscribeRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7697
        self.jobIds = {"type": "Vector.<uint>", "value": ""}
