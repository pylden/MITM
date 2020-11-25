from module.protocol.network.message import Message


class ServerSettingsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3435
        self.lang = {"type": "String", "value": ""}
        self.community = {"type": "uint", "value": ""}
        self.gameType = {"type": "int", "value": ""}
        self.isMonoAccount = {"type": "Boolean", "value": ""}
        self.arenaLeaveBanTime = {"type": "uint", "value": ""}
        self.itemMaxLevel = {"type": "uint", "value": ""}
        self.hasFreeAutopilot = {"type": "Boolean", "value": ""}
