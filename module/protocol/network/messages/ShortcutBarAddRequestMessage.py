from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarAddRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2373
        self.vars.append({"name": "barType", "type": "uint", "value": ""})
        self.vars.append({"name": "shortcut", "type": "Shortcut", "value": ""})
