from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorDialogQuestionBasicMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 778
        self.guildInfo = {"type": "BasicGuildInformations", "value": ""}
