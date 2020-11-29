from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ServerSettingsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3435
        self.vars.append({"name": "lang", "type": "String", "value": ""})
        self.vars.append({"name": "community", "type": "uint", "value": ""})
        self.vars.append({"name": "gameType", "type": "int", "value": ""})
        self.vars.append({"name": "isMonoAccount", "type": "Boolean", "value": ""})
        self.vars.append({"name": "arenaLeaveBanTime", "type": "uint", "value": ""})
        self.vars.append({"name": "itemMaxLevel", "type": "uint", "value": ""})
        self.vars.append({"name": "hasFreeAutopilot", "type": "Boolean", "value": ""})
