from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobCrafterDirectoryEntryMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3973
        self.vars.append({"name": "playerInfo", "type": "JobCrafterDirectoryEntryPlayerInfo", "value": ""})
        self.vars.append({"name": "jobInfoList", "type": "Vector.<JobCrafterDirectoryEntryJobInfo>", "value": ""})
        self.vars.append({"name": "playerLook", "type": "EntityLook", "value": ""})
