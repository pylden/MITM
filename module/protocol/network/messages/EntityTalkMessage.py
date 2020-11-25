from module.protocol.network.message import Message


class EntityTalkMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5442
        self.entityId = {"type": "Number", "value": ""}
        self.textId = {"type": "uint", "value": ""}
        self.parameters = {"type": "Vector.<String>", "value": ""}
