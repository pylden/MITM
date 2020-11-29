from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IdentificationSuccessMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8394
        self.vars.append({"name": "login", "type": "String", "value": ""})
        self.vars.append({"name": "nickname", "type": "String", "value": ""})
        self.vars.append({"name": "accountId", "type": "uint", "value": ""})
        self.vars.append({"name": "communityId", "type": "uint", "value": ""})
        self.vars.append({"name": "hasRights", "type": "Boolean", "value": ""})
        self.vars.append({"name": "hasConsoleRight", "type": "Boolean", "value": ""})
        self.vars.append({"name": "secretQuestion", "type": "String", "value": ""})
        self.vars.append({"name": "accountCreation", "type": "Number", "value": ""})
        self.vars.append({"name": "subscriptionElapsedDuration", "type": "Number", "value": ""})
        self.vars.append({"name": "subscriptionEndDate", "type": "Number", "value": ""})
        self.vars.append({"name": "wasAlreadyConnected", "type": "Boolean", "value": ""})
        self.vars.append({"name": "havenbagAvailableRoom", "type": "uint", "value": ""})
