from module.protocol.network.message import Message


class ExchangeCraftResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1988
        self.craftResult = {"type": "uint", "value": ""}
