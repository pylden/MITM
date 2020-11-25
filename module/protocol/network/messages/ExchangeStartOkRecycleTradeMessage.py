from module.protocol.network.message import Message


class ExchangeStartOkRecycleTradeMessage(Message):
    def __init__(self):
        self.id = 9490
