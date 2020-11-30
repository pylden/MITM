from module.protocol.network.messages.ExchangeStartedMessage import ExchangeStartedMessage


class ExchangeStartedWithStorageMessage(ExchangeStartedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeStartedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8605
        self.storageMaxSlot = {"type": "uint", "value": ""}
