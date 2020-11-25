function getIp(array) {
    var str = "";
    for (var i = 0; i < array.length; i++) {
        if (str != "") {
            str += ".";
        }
        str += array[i];
    }
    return str;
}

Interceptor.attach(Module.getExportByName('ws2_32', 'connect'), {
    onEnter: function(args) {
        var addr = new Uint8Array(args[1].add(4).readByteArray(4));
        var ip = getIp(addr);
        var list_ips = [
            "34.252.21.81",
            "52.17.231.202",
            "63.34.214.78",
            "172.65.221.57",
        ];
        if (list_ips.indexOf(ip) != -1) {
            args[1].writeByteArray([
                0x02, 0x00,
                0x15, 0xB3,
                0x7F, 0x00, 0x00, 0x01,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
            ]);
            send(ip)
        }
    }
});