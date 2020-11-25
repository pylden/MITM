from module.protocol.network.message import Message


class PrismUseRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6760
        self.moduleToUse = {"type": "uint", "value": ""}
