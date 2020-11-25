from module.protocol.network.message import Message


class AbstractGameActionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3972
        self.actionId = {"type": "uint", "value": ""}
        self.sourceId = {"type": "Number", "value": ""}
