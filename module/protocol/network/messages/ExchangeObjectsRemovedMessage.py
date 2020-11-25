from module.protocol.network.message import Message


class ExchangeObjectsRemovedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5450
        self.objectUID = {"type": "Vector.<uint>", "value": ""}
