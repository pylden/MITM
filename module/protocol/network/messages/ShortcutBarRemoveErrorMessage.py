from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarRemoveErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5768
        self.vars.append({"name": "error", "type": "uint", "value": ""})
