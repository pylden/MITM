from module.protocol.network.message import Message


class GuildVersatileInfoListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9944
        self.guilds = {"type": "Vector.<GuildVersatileInformations>", "value": ""}
