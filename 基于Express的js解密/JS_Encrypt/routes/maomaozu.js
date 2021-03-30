var CryptoJS = require("crypto-js");
function timest() {
    var tmp = Date.parse( new Date() ).toString();
    tmp = tmp.substr(0,10);
    return tmp;
}
function payload() {
    e = '55b3b62613aef1a0';
    l = "\{\"expire\"\:"+timest() +"\}";
    console.log(l)
    return e = CryptoJS.enc.Utf8.parse(e),
        l = CryptoJS.enc.Utf8.parse(l),
        CryptoJS.AES.encrypt(l, e, {
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7,
            iv: e
        }).toString()
}

function decrypt(i) {
    e = '0a1fea31626b3b55';
    l = i;
    e = CryptoJS.enc.Utf8.parse(e);
    var a = CryptoJS.AES.decrypt(l, e, {
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7,
        iv: e
    });
    // console.log(a)
    return CryptoJS.enc.Utf8.stringify(a).toString()
}
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    res.send(payload());
});
router.post('/decrypt', function(req, res, next) {
    var result = req.body
    res.send(decrypt(result.data));
});

module.exports = router;
