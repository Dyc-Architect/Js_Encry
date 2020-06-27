var CryptoJS = require("./crypto-js-4.0.0");

function aes(content) {
    var password_input, encrypt_iv, encrypt_key;
    var o = CryptoJS.MD5(Math.random() + "").toString();
    for (t = CryptoJS.AES.encrypt(content, o, {
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    }),
             password_encode = t.ciphertext.toString(CryptoJS.enc.Base64); password_input != password_encode; )

    password_input = password_encode;
    encrypt_iv = t.iv.toString(CryptoJS.enc.Base64),
    encrypt_key = t.key.toString(CryptoJS.enc.Base64);
    e = 16;
    for (var t = "", n = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", o = 0; e > o; o++)
        t += n.charAt(Math.floor(Math.random() * n.length));


    return JSON.stringify({
        password: password_input,
        encrypt_iv: encrypt_iv,
        encrypt_key: encrypt_key,
        dsc_token: t
    })
}
console.log(aes("111111"))