from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildChangeMemberParametersMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2513
        self.vars.append({"name": "memberId", "type": "Number", "value": ""})
        self.vars.append({"name": "rank", "type": "uint", "value": ""})
        self.vars.append({"name": "experienceGivenPercent", "type": "uint", "value": ""})
        self.vars.append({"name": "rights", "type": "uint", "value": ""})
