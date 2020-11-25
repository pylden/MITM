from module.protocol.network.message import Message
from module.io.BytesReader import BytesReader
from module.protocol.network.messages_dict import MessagesDict


class MessageFactory:
    def message(buffer):
        if len(buffer) < 8:  # If the current buffer is not even the size of header
            return None

        buffer_reader = BytesReader(buffer)
        hi_header = buffer_reader.read(2)
        id = int.from_bytes(hi_header, 'big') >> 2
        len_type_tmp = int.from_bytes(hi_header, 'big') & 3
        length = 0
        while len_type_tmp:
            length = (length << 8) + int.from_bytes(buffer_reader.read(1), 'big')
            len_type_tmp -= 1

        if buffer_reader.get_current_buffer().nbytes < length:  # If the current buffer is small than the packet length.
            return None

        return MssagesDict(id)(buffer_reader)

    message = staticmethod(message)
