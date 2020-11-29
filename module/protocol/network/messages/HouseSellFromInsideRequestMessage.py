from module.protocol.network.messages.HouseSellRequestMessage import HouseSellRequestMessage


class HouseSellFromInsideRequestMessage(HouseSellRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        HouseSellRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8376
