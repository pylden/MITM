from module.protocol.network.message import Message


class ServerSessionConstantsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9947
        self.variables = {"type": "Vector.<ServerSessionConstant>", "value": ""}
