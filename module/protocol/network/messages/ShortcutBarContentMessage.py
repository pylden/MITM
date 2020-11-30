from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarContentMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 400
        self.barType = {"type": "uint", "value": ""}
        self.shortcuts = {"type": "Vector.<Shortcut>", "value": ""}
