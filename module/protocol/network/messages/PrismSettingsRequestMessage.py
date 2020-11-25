from module.protocol.network.message import Message


class PrismSettingsRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8733
        self.subAreaId = {"type": "uint", "value": ""}
        self.startDefenseTime = {"type": "uint", "value": ""}
