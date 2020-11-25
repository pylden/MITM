from module.protocol.network.message import Message


class ExchangeObjectModifiedInBagMessage(Message):
    def __init__(self):
        self.id = 6601
