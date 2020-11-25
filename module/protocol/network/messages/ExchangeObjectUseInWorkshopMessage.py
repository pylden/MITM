from module.protocol.network.message import Message


class ExchangeObjectUseInWorkshopMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2394
        self.objectUID = {"type": "uint", "value": ""}
        self.quantity = {"type": "int", "value": ""}
