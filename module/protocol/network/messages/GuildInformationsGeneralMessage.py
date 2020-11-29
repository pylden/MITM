from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildInformationsGeneralMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5234
        self.vars.append({"name": "abandonnedPaddock", "type": "Boolean", "value": ""})
        self.vars.append({"name": "level", "type": "uint", "value": ""})
        self.vars.append({"name": "expLevelFloor", "type": "Number", "value": ""})
        self.vars.append({"name": "experience", "type": "Number", "value": ""})
        self.vars.append({"name": "expNextLevelFloor", "type": "Number", "value": ""})
        self.vars.append({"name": "creationDate", "type": "uint", "value": ""})
        self.vars.append({"name": "nbTotalMembers", "type": "uint", "value": ""})
        self.vars.append({"name": "nbConnectedMembers", "type": "uint", "value": ""})
