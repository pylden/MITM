from module.protocol.network.message import Message


class RecycleResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3014
        self.nuggetsForPrism = {"type": "uint", "value": ""}
        self.nuggetsForPlayer = {"type": "uint", "value": ""}
