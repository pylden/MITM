from module.protocol.network.message import Message


class PrismFightRemovedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6587
        self.subAreaId = {"type": "uint", "value": ""}
