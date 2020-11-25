from module.protocol.network.message import Message


class TaxCollectorAttackedResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8211
        self.deadOrAlive = {"type": "Boolean", "value": ""}
        self.basicInfos = {"type": "TaxCollectorBasicInformations", "value": ""}
        self.guild = {"type": "BasicGuildInformations", "value": ""}
