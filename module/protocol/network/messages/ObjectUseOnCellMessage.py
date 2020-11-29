from module.protocol.network.messages.ObjectUseMessage import ObjectUseMessage


class ObjectUseOnCellMessage(ObjectUseMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ObjectUseMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6871
        self.vars.append({"name": "cells", "type": "uint", "value": ""})
