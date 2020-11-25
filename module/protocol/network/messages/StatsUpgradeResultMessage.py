from module.protocol.network.message import Message


class StatsUpgradeResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4819
        self.result = {"type": "int", "value": ""}
        self.nbCharacBoost = {"type": "uint", "value": ""}
