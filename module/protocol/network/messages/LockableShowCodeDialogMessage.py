from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LockableShowCodeDialogMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1740
        self.vars.append({"name": "changeOrUse", "type": "Boolean", "value": ""})
        self.vars.append({"name": "codeSize", "type": "uint", "value": ""})
