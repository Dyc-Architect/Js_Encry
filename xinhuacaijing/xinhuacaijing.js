var CryptoJS = require("D:\\dyc\\JS\\新华财经\\crypto-js");
function L(t) {
    for (var i = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], e = "", n = 0; n < t; n++) {
        e += i[parseInt(9 * Math.random())]
    }
    return e
}
function get_hkey_value(id) {
    var t = "\{\"newsId\"\:\""+id+"\"\,\"appVersion\"\:\"string\"\,\"deviceId\"\:\"string\"\,\"ipAddress\"\:\"string\"\}";
    var i = L(32)
        , e = CryptoJS.enc.Utf8.parse(i)
        , n = CryptoJS.enc.Utf8.parse("1234567890123456")
        , s = CryptoJS.enc.Utf8.parse(t)
        , o = CryptoJS.AES.encrypt(s, e, {
        iv: n,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).ciphertext.toString().toUpperCase()
        , a = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Hex.parse(o)).replace(/\+/g, "-").replace(/\//g, "_")
        , r = L(32)
        , l = (CryptoJS.enc.Utf8.parse(r),
    i.slice(0, 16) + r.slice(16) + "#" + r.slice(0, 16) + i.slice(16))
        , c = CryptoJS.enc.Utf8.parse(l);
    return {
        hkey: CryptoJS.enc.Base64.stringify(c),
        value: a
    }
}
function dencrypt(t, i) {
            var e = CryptoJS.enc.Utf8.parse("1234567890123456")
              , n = CryptoJS.enc.Base64.parse(i).toString(CryptoJS.enc.Utf8)
              , s = n.slice(0, 16) + n.slice(49)
              , o = CryptoJS.enc.Utf8.parse(s)
              , a = CryptoJS.enc.Base64.parse(t)
              , r = CryptoJS.enc.Base64.stringify(a);
            return CryptoJS.AES.decrypt(r, o, {
                iv: e,
                mode:CryptoJS.mode.CBC,
                padding: CryptoJS.pad.Pkcs7
            }).toString(CryptoJS.enc.Utf8).toString()
        }
