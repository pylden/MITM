from module.protocol.network.messages.NetworkMessage import NetworkMessage


class QuestValidatedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5469
        self.vars.append({"name": "questId", "type": "uint", "value": ""})
