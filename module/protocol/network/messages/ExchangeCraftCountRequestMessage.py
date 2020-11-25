from module.protocol.network.message import Message


class ExchangeCraftCountRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6588
        self.count = {"type": "int", "value": ""}
