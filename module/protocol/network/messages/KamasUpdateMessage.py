from module.protocol.network.message import Message


class KamasUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2022
        self.kamasTotal = {"type": "Number", "value": ""}
