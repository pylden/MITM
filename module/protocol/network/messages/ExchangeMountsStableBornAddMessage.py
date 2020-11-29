from module.protocol.network.messages.ExchangeMountsStableAddMessage import ExchangeMountsStableAddMessage


class ExchangeMountsStableBornAddMessage(ExchangeMountsStableAddMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeMountsStableAddMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8651
