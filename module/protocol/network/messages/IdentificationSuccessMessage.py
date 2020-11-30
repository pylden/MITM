from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IdentificationSuccessMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8394
        self.login = {"type": "String", "value": ""}
        self.nickname = {"type": "String", "value": ""}
        self.accountId = {"type": "uint", "value": ""}
        self.communityId = {"type": "uint", "value": ""}
        self.hasRights = {"type": "Boolean", "value": ""}
        self.hasConsoleRight = {"type": "Boolean", "value": ""}
        self.secretQuestion = {"type": "String", "value": ""}
        self.accountCreation = {"type": "Number", "value": ""}
        self.subscriptionElapsedDuration = {"type": "Number", "value": ""}
        self.subscriptionEndDate = {"type": "Number", "value": ""}
        self.wasAlreadyConnected = {"type": "Boolean", "value": ""}
        self.havenbagAvailableRoom = {"type": "uint", "value": ""}
