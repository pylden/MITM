from module.protocol.processor.protocol_processor import ProtocolProcessor
from module.protocol.message.packet_factory import PacketFactory


class D2Protocol(ProtocolProcessor):
    def get_packets(buffer, data):
        buffer += data
        packets = list()
        while packet := PacketFactory.packet(buffer):
            packets.append(packet)
            buffer = buffer[packet.get_packet_size():]
        return packets, buffer

    def from_client(self, data):
        packets, self._client_buffer = self.get_packets(self._client_buffer, data)
        if len(packets):
            print("From client:")
            for packet in packets:
                print(packet)

    def from_server(self, data):
        packets, self._server_buffer = self.get_packets(self._server_buffer, data)
        if len(packets):
            print("From server:")
            for packet in packets:
                print(packet)

    get_packets = staticmethod(get_packets)
