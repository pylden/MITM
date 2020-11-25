from module.protocol.network.message import Message


class JobCrafterDirectoryEntryMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3973
        self.playerInfo = {"type": "JobCrafterDirectoryEntryPlayerInfo", "value": ""}
        self.jobInfoList = {"type": "Vector.<JobCrafterDirectoryEntryJobInfo>", "value": ""}
        self.playerLook = {"type": "EntityLook", "value": ""}
