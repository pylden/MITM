from module.protocol.network.message import Message


class PrismFightStateUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1999
        self.state = {"type": "uint", "value": ""}
