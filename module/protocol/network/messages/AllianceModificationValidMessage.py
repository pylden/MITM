from module.protocol.network.message import Message


class AllianceModificationValidMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8871
        self.allianceName = {"type": "String", "value": ""}
        self.allianceTag = {"type": "String", "value": ""}
        self.Alliancemblem = {"type": "GuildEmblem", "value": ""}
