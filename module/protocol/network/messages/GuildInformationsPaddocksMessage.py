from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildInformationsPaddocksMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6791
        self.nbPaddockMax = {"type": "uint", "value": ""}
        self.paddocksInformations = {"type": "Vector.<PaddockContentInformations>", "value": ""}
