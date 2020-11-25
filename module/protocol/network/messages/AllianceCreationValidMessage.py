from module.protocol.network.message import Message


class AllianceCreationValidMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8739
        self.allianceName = {"type": "String", "value": ""}
        self.allianceTag = {"type": "String", "value": ""}
        self.allianceEmblem = {"type": "GuildEmblem", "value": ""}
