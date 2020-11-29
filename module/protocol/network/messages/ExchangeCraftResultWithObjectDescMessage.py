from module.protocol.network.messages.ExchangeCraftResultMessage import ExchangeCraftResultMessage


class ExchangeCraftResultWithObjectDescMessage(ExchangeCraftResultMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeCraftResultMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8570
        self.vars.append({"name": "objectInfo", "type": "ObjectItemNotInContainer", "value": ""})
