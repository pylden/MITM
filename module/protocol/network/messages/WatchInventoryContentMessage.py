from module.protocol.network.messages.InventoryContentMessage import InventoryContentMessage


class WatchInventoryContentMessage(InventoryContentMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        InventoryContentMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7807
