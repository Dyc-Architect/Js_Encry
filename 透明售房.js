var Crypto  = require("./crypto-js")
function w(a, d) {
    this["key"] = a;
    this["value"] = d
}
function getmoreinfomation() {
    return [{key: "webSmartID", value: "3b83b5036343d892aa8ce313f4fdb983"},{key: "touchSupport", value: "99115dfb07133750ba677d055874de87"},
        {key: "sessionStorage", value: "1"},{key: "localStorage", value: "1"},{key: "indexedDb", value: "1"},{key: "openDatabase", value: "1"},
        {key: "doNotTrack", value: "unknown"},{key: "plugins", value: "d22ca0b81584fbea62237b14bd04c866"},{key: "adblock", value: "0"},
        {key: "hasLiedLanguages", value: "false"},{key: "hasLiedResolution", value: "false"},{key: "hasLiedOs", value: "false"},
        {key: "hasLiedBrowser", value: "false"},{key: "jsFonts", value: "38437f3289ca7a613bb292a3de0dba2b"}]
}
function getSendPlatform() {
    return new w("platform","WEB")
}
function getCustId() {
    return new w("custID","88")
}
function getHistoryList() {
    return new w("historyList",1)
}
function getFlashVersion() {

    return new w("flashVersion",0)
}
function getTimeZone() {

    return new w("timeZone",-8)
}
function getUserLanguage() {

    return new w("userLanguage","")
}
function getSystemLanguage() {

    return new w("systemLanguage","")
}
function getOnLine() {
    return new w("onLine","" + "true")
}
function getCpuClass() {

    return new w("cpuClass","")
}
function getCookieEnabled() {
    return new w("cookieEnabled","1")
}
function getBrowserLanguage() {

    return new w("browserLanguage","zh-CN")
}
function getAppMinorVersion() {

    return  new w("appMinorVersion","a")
}
function getPlatform() {
    return new w("os","" + "Win32")
}
function getMimeTypes() {
    return new w("mimeTypes","52d67b2a5aa5e031084733d5006cc664")
}
function getJavaEnabled() {
    return new w("javaEnabled","0")
}
function getAppName() {
    return new w("appName","" + "Netscape")
}
function getAppCodeName() {
    return new w("appCodeName","" + "Mozilla")
}
function getScrDeviceXDPI() {
    return new w("scrDeviceXDPI","")
}
function md5ScrColorDepth() {
    return new w("scrColorDepth","" + 24)
}
function getScrAvailWidth() {
    return new w("scrAvailWidth","" + 1920)
}
function getScrAvailHeight() {
    return new w("scrAvailHeight","" + 1040)
}
function getScrWidth() {
    return new w("scrWidth","" + 1920)
}
function getScrHeight() {
    return new w("scrHeight","" + 1080)
}
function getUserAgent() {
    var a = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36";
    return a = a["replace"](/\&|\+/g, ""),
        new w("userAgent","" + a)
}
function getUUID() {
    return new w("UUID","new")
}

function getMachineCode() {
    return [getUUID(), getUserAgent(), getScrHeight(), getScrWidth(), getScrAvailHeight(), getScrAvailWidth(), md5ScrColorDepth(), getScrDeviceXDPI(), getAppCodeName(), getAppName(), getJavaEnabled(), getMimeTypes(), getPlatform(), getAppMinorVersion(), getBrowserLanguage(), getCookieEnabled(), getCpuClass(), getOnLine(), getSystemLanguage(), getUserLanguage(), getTimeZone(), getFlashVersion(), getHistoryList(), getCustId(), getSendPlatform()]
}
function getpackStr(a) {
    var e = [], e = [];
    e = getMachineCode(),
        e = e["concat"](getmoreinfomation()),
    null != a && void 0 != a && "" != a && 32 == a[m] && e[g](new w(Qj,a));
    a = {};
    for (k = 0; e["length"] > k; k++)
        // console.log(e[k]["key"])
        a[e[k]["key"]] ? e["splice"](k, 1) : a[e[k]["key"]] = !0;
    // console.log(k)
    return e["sort"](function(a, b) {
        var e, f;
        if ("object" == typeof a && "object" == typeof b && a && b)
            return e = a["key"],
                f = b["key"],
                e === f ? 0 : typeof e == typeof f ? f > e ? -1 : 1 : typeof f > typeof e ? -1 : 1;
        throw Pj;
    }),
        e
}
function xd(a) {
    for (var c = "", h = a["length"] - 1; 0 <= h; h--)
        c += a["charAt"](h);
    return c
}
function ha(a, f, g) {
    // console.log(a)
    for (var e = {}, k = 0; a["length"] > k; k++)
        e[a[k]["key"]] ? a["splice"](k, 1) : e[a[k]["key"]] = !0;
    a["sort"](function(a, b) {
        var e, f;
        if ("object" == typeof a && "object" == typeof b && a && b)
            return e = a["key"],
                f = b["key"],
                e === f ? 0 : typeof e == typeof f ? f > e ? -1 : 1 : typeof f > typeof e ? -1 : 1;
        throw "error";
    });
    for (e = 0; a["length"] > e; e++) {
        var k = a[e]["key"]["replace"](RegExp("%", "gm"), "")
            , n = "";
        if (n = "string" == typeof a[e]["value"] ? a[e]["value"]["replace"](RegExp("%", "gm"), "") : a[e]["value"],
        "" !== n)
            switch (g += k + n,
                n = encodeURIComponent(n),
                "WEB") {
                default:
                    jk = {adblock: "FMQw",
                        appMinorVersion: "qBVW",
                        appcodeName: "qT7b",
                        browserLanguage: "q4f3",
                        browserName: "-UVA",
                        browserVersion: "d435",
                        cookieCode: "VySQ",
                        cookieEnabled: "VPIf",
                        cpuClass: "Md7A",
                        doNotTrack: "VEek",
                        flashVersion: "dzuS",
                        hasLiedBrowser: "2xC5",
                        hasLiedLanguages: "j5po",
                        hasLiedOs: "ci5c",
                        hasLiedResolution: "3neK",
                        historyList: "kU5z",
                        indexedDb: "3sw-",
                        javaEnabled: "yD16",
                        jsFonts: "EOQP",
                        localCode: "lEnu",
                        localStorage: "XM7l",
                        mimeTypes: "jp76",
                        online: "9vyE",
                        openDatabase: "V8vl",
                        os: "hAqN",
                        plugins: "ks0Q",
                        scrAvailHeight: "88tV",
                        scrAvailSize: "TeRS",
                        scrAvailWidth: "E-lJ",
                        scrColorDepth: "qmyu",
                        scrDeviceXDPI: "3jCe",
                        scrHeight: "5Jwy",
                        scrWidth: "ssI5",
                        sessionStorage: "HVia",
                        srcScreenSize: "tOHY",
                        storeDb: "Fvje",
                        systemLanguage: "e6OK",
                        timeZone: "q5aJ",
                        touchSupport: "wNLf",
                        userAgent: "0aew",
                        userLanguage: "hLzX",
                        webSmartID: "E3gR"}
                    f += "&" + (void 0 == jk[k] ? k : jk[k]) + "=" + n
            }
    }
    a = g;
    g = a["length"];
    e = 0 == g % 3 ? parseInt(g / 3) : parseInt(g / 3) + 1;
    3 > g || (k = a["substring"](0, 1 * e),
        a = a["substring"](1 * e, 2 * e) + a["substring"](2 * e, g) + k);
    a = xd(a);
    a = xd(a);
    g = a["length"];
    e = a["split"]("");
    for (k = 0; parseInt(g / 2) > k; k++)
        0 == k % 2 && (n = a["charAt"](k),
            e[k] = e[g - 1 - k],
            e[g - 1 - k] = n);
    a = e["join"]("");
    g = Crypto.SHA256(a)["toString"](Crypto["enc"]["Base64"]);
    return g = Crypto.SHA256(g)["toString"](Crypto["enc"]["Base64"]),
        new w(f,g)
}
function generateData() {
    var e = "?algID=UvWLRDjuIE"
        , q = ""
        , n = ""
        , t = getpackStr();
    f = [];
    XE =["appCodeName", "appMinorVersion", "appName", "cpuClass", "onLine", "systemLanguage", "userLanguage", "historyList", "hasLiedLanguages", "hasLiedResolution", "hasLiedOs", "hasLiedBrowser"];
    YE = ["sessionStorage", "localStorage", "indexedDb", "openDatabase"];
    ZE = ["scrAvailWidth", "scrAvailHeight"];
    $E = ["scrDeviceXDPI", "scrColorDepth", "scrWidth", "scrHeight"]
    for (var r = [], v = [], x = [], u = 0; t["length"] > u; u++)
        "new" != t[u]["value"] && -1 == XE["indexOf"](t[u]["key"]) && (-1 == YE["indexOf"](t[u]["key"]) ? -1 == ZE["indexOf"](t[u]["key"]) ? -1 == $E["indexOf"](t[u]["key"]) ? f["push"](t[u]) : x["push"](t[u]) : v["push"](t[u]) : r["push"](t[u]));
    t = "";
    for (u = 0; r["length"] > u; u++)
        t = t + r[u]["key"]["charAt"](0) + r[u]["value"];
    r = "";
    for (u = 0; x["length"] > u; u++)
        0 == u ? r += x[u]["value"] : r = r + "x" + x[u]["value"];
    x = "";
    for (u = 0; v["length"] > u; u++)
        0 == u ? x += v[u]["value"] : x = x + "x" + v[u]["value"];
    f["push"](new w("storeDb",t));
    f["push"](new w("srcScreenSize",r));
    f["push"](new w("scrAvailSize",x));
    n = ha(f, q, n);
    q = n["key"];
    n = n["value"];
    k = new Date;
    q += "&timestamp=" + k["getTime"]();
    e = e + "&hashCode=" + n + q;
    return e
}
console.log(generateData())