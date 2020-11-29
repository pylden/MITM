from module.protocol.network.messages.ExchangeBidHouseInListAddedMessage import ExchangeBidHouseInListAddedMessage


class ExchangeBidHouseInListUpdatedMessage(ExchangeBidHouseInListAddedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeBidHouseInListAddedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5016
