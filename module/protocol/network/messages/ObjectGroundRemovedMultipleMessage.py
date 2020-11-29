from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObjectGroundRemovedMultipleMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3658
        self.vars.append({"name": "cells", "type": "Vector.<uint>", "value": ""})
