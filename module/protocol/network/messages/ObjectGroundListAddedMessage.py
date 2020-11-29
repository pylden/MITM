from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObjectGroundListAddedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1696
        self.vars.append({"name": "cells", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "referenceIds", "type": "Vector.<uint>", "value": ""})
