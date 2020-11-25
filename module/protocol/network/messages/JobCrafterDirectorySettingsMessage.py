from module.protocol.network.message import Message


class JobCrafterDirectorySettingsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4100
        self.craftersSettings = {"type": "Vector.<JobCrafterDirectorySettings>", "value": ""}
