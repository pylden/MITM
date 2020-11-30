from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildVersatileInfoListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9944
        self.guilds = {"type": "Vector.<GuildVersatileInformations>", "value": ""}
