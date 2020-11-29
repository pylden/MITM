from module.protocol.network.messages.NetworkMessage import NetworkMessage


class InteractiveElementUpdatedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2801
        self.vars.append({"name": "interactiveElement", "type": "InteractiveElement", "value": ""})
