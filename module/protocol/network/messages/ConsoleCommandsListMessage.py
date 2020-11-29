from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ConsoleCommandsListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1923
        self.vars.append({"name": "aliases", "type": "Vector.<String>", "value": ""})
        self.vars.append({"name": "args", "type": "Vector.<String>", "value": ""})
        self.vars.append({"name": "descriptions", "type": "Vector.<String>", "value": ""})
