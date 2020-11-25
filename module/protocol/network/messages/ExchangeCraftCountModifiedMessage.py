from module.protocol.network.message import Message


class ExchangeCraftCountModifiedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3547
        self.count = {"type": "int", "value": ""}
