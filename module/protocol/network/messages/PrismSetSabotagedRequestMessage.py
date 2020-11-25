from module.protocol.network.message import Message


class PrismSetSabotagedRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9154
        self.subAreaId = {"type": "uint", "value": ""}
