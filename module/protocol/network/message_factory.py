from module.io.bytes_reader import BytesReader
from module.protocol.network.messages_dict import MessagesDict


class MessageFactory:
    def message(buffer, from_client=False):
        buffer_reader = BytesReader(buffer)

        if buffer_reader.get_current_buffer().nbytes < 2:  # If the current buffer is not even the size of header
            print("Header too small: %s" % buffer_reader.getbuffer().hex())
            return None

        hi_header = buffer_reader.read(2)
        count = None if not from_client else buffer_reader.read_uint()
        id = int.from_bytes(hi_header, 'big') >> 2
        len_type = int.from_bytes(hi_header, 'big') & 3

        if buffer_reader.get_current_buffer().nbytes < len_type:
            print("Packet too small 1")
            return None

        length = int.from_bytes(buffer_reader.read(len_type), 'big')

        if buffer_reader.get_current_buffer().nbytes < length:  # If the current buffer is small than the packet length.
            print("Packet too small 2")
            return None

        msg = buffer_reader.read(length)

        try:
            msg = MessagesDict[id](BytesReader(msg), len_type, length, count=count)
        except KeyError:
            print("ID not found: %d" % id)
            exit()
        try:
            msg.deserialize()
        except Exception:
            print("Can't deserialize")
        return msg
    message = staticmethod(message)
