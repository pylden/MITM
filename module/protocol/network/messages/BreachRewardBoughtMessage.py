from module.protocol.network.message import Message


class BreachRewardBoughtMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 288
        self.id = {"type": "uint", "value": ""}
        self.bought = {"type": "Boolean", "value": ""}
