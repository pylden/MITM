from module.protocol.network.message import Message


class PrismFightStateUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1999
        self.state = {"type": "uint", "value": ""}
