from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TeleportToBuddyOfferMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5460
        self.dungeonId = {"type": "uint", "value": ""}
        self.buddyId = {"type": "Number", "value": ""}
        self.timeLeft = {"type": "uint", "value": ""}
