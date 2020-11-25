from module.protocol.network.message import Message


class StatsUpgradeResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4819
        self.result = {"type": "int", "value": ""}
        self.nbCharacBoost = {"type": "uint", "value": ""}
