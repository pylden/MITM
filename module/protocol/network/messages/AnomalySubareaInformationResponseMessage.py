from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AnomalySubareaInformationResponseMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8393
        self.subareas = {"type": "Vector.<AnomalySubareaInformation>", "value": ""}
