from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TeleportToBuddyOfferMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5460
        self.vars.append({"name": "dungeonId", "type": "uint", "value": ""})
        self.vars.append({"name": "buddyId", "type": "Number", "value": ""})
        self.vars.append({"name": "timeLeft", "type": "uint", "value": ""})
