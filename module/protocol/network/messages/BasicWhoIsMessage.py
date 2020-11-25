from module.protocol.network.message import Message


class BasicWhoIsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6352
        self.self = {"type": "Boolean", "value": ""}
        self.position = {"type": "int", "value": ""}
        self.accountNickname = {"type": "String", "value": ""}
        self.accountId = {"type": "uint", "value": ""}
        self.playerName = {"type": "String", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
        self.areaId = {"type": "int", "value": ""}
        self.serverId = {"type": "int", "value": ""}
        self.originServerId = {"type": "int", "value": ""}
        self.socialGroups = {"type": "Vector.<AbstractSocialGroupInfos>", "value": ""}
        self.verbose = {"type": "Boolean", "value": ""}
        self.playerState = {"type": "uint", "value": ""}
