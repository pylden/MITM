from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorAttackedResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8211
        self.deadOrAlive = {"type": "Boolean", "value": ""}
        self.basicInfos = {"type": "TaxCollectorBasicInformations", "value": ""}
        self.guild = {"type": "BasicGuildInformations", "value": ""}
