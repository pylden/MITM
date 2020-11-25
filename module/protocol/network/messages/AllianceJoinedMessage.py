from module.protocol.network.message import Message


class AllianceJoinedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6500
        self.allianceInfo = {"type": "AllianceInformations", "value": ""}
        self.enabled = {"type": "Boolean", "value": ""}
        self.leadingGuildId = {"type": "uint", "value": ""}
