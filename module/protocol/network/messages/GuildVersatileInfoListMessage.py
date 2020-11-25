from module.protocol.network.message import Message


class GuildVersatileInfoListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9944
        self.guilds = {"type": "Vector.<GuildVersatileInformations>", "value": ""}
