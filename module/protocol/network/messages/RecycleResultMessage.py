from module.protocol.network.message import Message


class RecycleResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3014
        self.nuggetsForPrism = {"type": "uint", "value": ""}
        self.nuggetsForPlayer = {"type": "uint", "value": ""}
