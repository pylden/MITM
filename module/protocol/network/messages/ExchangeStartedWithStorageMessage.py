from module.protocol.network.message import Message


class ExchangeStartedWithStorageMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8605
        self.storageMaxSlot = {"type": "uint", "value": ""}
