from module.protocol.network.messages.ExchangeCraftResultWithObjectIdMessage import ExchangeCraftResultWithObjectIdMessage


class ExchangeCraftInformationObjectMessage(ExchangeCraftResultWithObjectIdMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeCraftResultWithObjectIdMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2393
        self.vars.append({"name": "playerId", "type": "Number", "value": ""})
