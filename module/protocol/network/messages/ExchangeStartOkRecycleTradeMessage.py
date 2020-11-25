from module.protocol.network.message import Message


class ExchangeStartOkRecycleTradeMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9490
        self.percentToPrism = {"type": "uint", "value": ""}
        self.percentToPlayer = {"type": "uint", "value": ""}
