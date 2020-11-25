from module.protocol.network.message import Message


class KamasUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2022
        self.kamasTotal = {"type": "Number", "value": ""}
