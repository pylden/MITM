from module.protocol.network.message import Message


class ExchangeObjectTransfertListWithQuantityToInvMessage(Message):
    def __init__(self):
        self.id = 3741