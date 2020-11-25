from module.protocol.network.message import Message


class AllianceCreationVal8739(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8739
        self.allianceName = {"type": "String", "value": ""}
        self.allianceTag = {"type": "String", "value": ""}
        self.allianceEmblem = {"type": "GuildEmblem", "value": ""}
