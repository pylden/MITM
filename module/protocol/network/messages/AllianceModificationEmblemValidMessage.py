from module.protocol.network.message import Message


class AllianceModificationEmblemVal2632(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2632
        self.Alliancemblem = {"type": "GuildEmblem", "value": ""}
