from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BasicWhoIsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6352
        self.vars.append({"name": "self", "type": "Boolean", "value": ""})
        self.vars.append({"name": "position", "type": "int", "value": ""})
        self.vars.append({"name": "accountNickname", "type": "String", "value": ""})
        self.vars.append({"name": "accountId", "type": "uint", "value": ""})
        self.vars.append({"name": "playerName", "type": "String", "value": ""})
        self.vars.append({"name": "playerId", "type": "Number", "value": ""})
        self.vars.append({"name": "areaId", "type": "int", "value": ""})
        self.vars.append({"name": "serverId", "type": "int", "value": ""})
        self.vars.append({"name": "originServerId", "type": "int", "value": ""})
        self.vars.append({"name": "socialGroups", "type": "Vector.<AbstractSocialGroupInfos>", "value": ""})
        self.vars.append({"name": "verbose", "type": "Boolean", "value": ""})
        self.vars.append({"name": "playerState", "type": "uint", "value": ""})
