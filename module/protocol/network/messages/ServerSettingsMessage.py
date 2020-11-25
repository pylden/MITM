from module.protocol.network.message import Message


class ServerSettingsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3435
        self.lang = {"type": "String", "value": ""}
        self.community = {"type": "uint", "value": ""}
        self.gameType = {"type": "int", "value": ""}
        self.isMonoAccount = {"type": "Boolean", "value": ""}
        self.arenaLeaveBanTime = {"type": "uint", "value": ""}
        self.itemMaxLevel = {"type": "uint", "value": ""}
        self.hasFreeAutopilot = {"type": "Boolean", "value": ""}
