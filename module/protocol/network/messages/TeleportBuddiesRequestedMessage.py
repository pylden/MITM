from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TeleportBuddiesRequestedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9376
        self.vars.append({"name": "dungeonId", "type": "uint", "value": ""})
        self.vars.append({"name": "inviterId", "type": "Number", "value": ""})
        self.vars.append({"name": "invalidBuddiesIds", "type": "Vector.<Number>", "value": ""})
