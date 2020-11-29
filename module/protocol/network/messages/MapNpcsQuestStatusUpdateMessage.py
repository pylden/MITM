from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapNpcsQuestStatusUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1168
        self.vars.append({"name": "mapId", "type": "Number", "value": ""})
        self.vars.append({"name": "npcsIdsWithQuest", "type": "Vector.<int>", "value": ""})
        self.vars.append({"name": "questFlags", "type": "Vector.<GameRolePlayNpcQuestFlag>", "value": ""})
        self.vars.append({"name": "npcsIdsWithoutQuest", "type": "Vector.<int>", "value": ""})
