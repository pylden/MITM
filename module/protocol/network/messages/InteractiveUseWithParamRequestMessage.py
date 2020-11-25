from module.protocol.network.message import Message


class InteractiveUseWithParamRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4240
        self.id = {"type": "int", "value": ""}
