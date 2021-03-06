from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HaapiBufferListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7471
        self.buffers = {"type": "Vector.<BufferInformation>", "value": ""}
