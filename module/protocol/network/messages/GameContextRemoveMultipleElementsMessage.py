from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameContextRemoveMultipleElementsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3474
        self.vars.append({"name": "elementsIds", "type": "Vector.<Number>", "value": ""})
