from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LockableShowCodeDialogMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1740
        self.changeOrUse = {"type": "Boolean", "value": ""}
        self.codeSize = {"type": "uint", "value": ""}
