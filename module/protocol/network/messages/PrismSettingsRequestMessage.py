from module.protocol.network.message import Message


class PrismSettingsRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8733
        self.subAreaId = {"type": "uint", "value": ""}
        self.startDefenseTime = {"type": "uint", "value": ""}
