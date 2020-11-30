from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobCrafterDirectorySettingsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4100
        self.craftersSettings = {"type": "Vector.<JobCrafterDirectorySettings>", "value": ""}
