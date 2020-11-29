from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TextInformationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5636
        self.vars.append({"name": "msgType", "type": "uint", "value": ""})
        self.vars.append({"name": "msgId", "type": "uint", "value": ""})
        self.vars.append({"name": "parameters", "type": "Vector.<String>", "value": ""})
