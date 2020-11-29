from module.protocol.network.messages.NetworkMessage import NetworkMessage


class RefreshFollowedQuestsOrderRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8535
        self.vars.append({"name": "quests", "type": "Vector.<uint>", "value": ""})
