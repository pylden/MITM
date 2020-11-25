from module.protocol.network.message import Message


class StatsUpgradeRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2014
        self.useAdditionnal = {"type": "Boolean", "value": ""}
        self.statId = {"type": "uint", "value": ""}
        self.boostPoint = {"type": "uint", "value": ""}
