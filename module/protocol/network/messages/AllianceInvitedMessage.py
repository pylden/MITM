from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceInvitedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6002
        self.vars.append({"name": "recruterId", "type": "Number", "value": ""})
        self.vars.append({"name": "recruterName", "type": "String", "value": ""})
        self.vars.append({"name": "allianceInfo", "type": "BasicNamedAllianceInformations", "value": ""})
