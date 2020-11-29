from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IdentificationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5833
        self.vars.append({"name": "version", "type": "Version", "value": ""})
        self.vars.append({"name": "lang", "type": "String", "value": ""})
        self.vars.append({"name": "credentials", "type": "Vector.<int>", "value": ""})
        self.vars.append({"name": "serverId", "type": "int", "value": ""})
        self.vars.append({"name": "autoconnect", "type": "Boolean", "value": ""})
        self.vars.append({"name": "useCertificate", "type": "Boolean", "value": ""})
        self.vars.append({"name": "useLoginToken", "type": "Boolean", "value": ""})
        self.vars.append({"name": "sessionOptionalSalt", "type": "Number", "value": ""})
        self.vars.append({"name": "failedAttempts", "type": "Vector.<uint>", "value": ""})
