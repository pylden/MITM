from module.protocol.network.message import Message


class PrismSetSabotagedRefusedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1834
        self.subAreaId = {"type": "uint", "value": ""}
        self.reason = {"type": "int", "value": ""}
