from module.protocol.network.message import Message


class GuildListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 641
        self.guilds = {"type": "Vector.<GuildInformations>", "value": ""}
