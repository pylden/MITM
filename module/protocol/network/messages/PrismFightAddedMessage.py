from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismFightAddedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9780
        self.fight = {"type": "PrismFightersInformation", "value": ""}
