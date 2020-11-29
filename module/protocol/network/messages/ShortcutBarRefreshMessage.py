from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarRefreshMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9875
        self.vars.append({"name": "barType", "type": "uint", "value": ""})
        self.vars.append({"name": "shortcut", "type": "Shortcut", "value": ""})
