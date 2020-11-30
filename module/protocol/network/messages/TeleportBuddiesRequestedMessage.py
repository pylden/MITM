from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TeleportBuddiesRequestedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9376
        self.dungeonId = {"type": "uint", "value": ""}
        self.inviterId = {"type": "Number", "value": ""}
        self.invalidBuddiesIds = {"type": "Vector.<Number>", "value": ""}
