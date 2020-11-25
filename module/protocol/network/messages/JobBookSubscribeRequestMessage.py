from module.protocol.network.message import Message


class JobBookSubscribeRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7697
        self.jobIds = {"type": "Vector.<uint>", "value": ""}
