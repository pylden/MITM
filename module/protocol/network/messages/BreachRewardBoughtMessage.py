from module.protocol.network.message import Message


class BreachRewardBoughtMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 288
        self.id = {"type": "uint", "value": ""}
        self.bought = {"type": "Boolean", "value": ""}
