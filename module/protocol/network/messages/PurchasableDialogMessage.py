from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PurchasableDialogMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6734
        self.vars.append({"name": "buyOrSell", "type": "Boolean", "value": ""})
        self.vars.append({"name": "purchasableId", "type": "Number", "value": ""})
        self.vars.append({"name": "purchasableInstanceId", "type": "uint", "value": ""})
        self.vars.append({"name": "secondHand", "type": "Boolean", "value": ""})
        self.vars.append({"name": "price", "type": "Number", "value": ""})
