from module.protocol.network.message import Message


class TaxCollectorAttackedResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8211
        self.deadOrAlive = {"type": "Boolean", "value": ""}
        self.basicInfos = {"type": "TaxCollectorBasicInformations", "value": ""}
        self.guild = {"type": "BasicGuildInformations", "value": ""}
