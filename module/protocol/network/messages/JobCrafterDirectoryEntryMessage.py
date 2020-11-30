from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobCrafterDirectoryEntryMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3973
        self.playerInfo = {"type": "JobCrafterDirectoryEntryPlayerInfo", "value": ""}
        self.jobInfoList = {"type": "Vector.<JobCrafterDirectoryEntryJobInfo>", "value": ""}
        self.playerLook = {"type": "EntityLook", "value": ""}
