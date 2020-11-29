from module.protocol.network.messages.ExchangeCraftResultWithObjectDescMessage import ExchangeCraftResultWithObjectDescMessage


class ExchangeCraftResultMagicWithObjectDescMessage(ExchangeCraftResultWithObjectDescMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeCraftResultWithObjectDescMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 819
        self.vars.append({"name": "magicPoolStatus", "type": "int", "value": ""})
