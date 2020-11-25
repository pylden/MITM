from module.protocol.network.message import Message


class AllianceJoinedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6500
        self.allianceInfo = {"type": "AllianceInformations", "value": ""}
        self.enabled = {"type": "Boolean", "value": ""}
        self.leadingGuildId = {"type": "uint", "value": ""}
