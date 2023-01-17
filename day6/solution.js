"use strict";
exports.__esModule = true;
var fs = require("fs");
fs.readFile("./input.txt", "utf8", function (err, data) {
    if (err) {
        return;
    }
    var input = data;
    var windL = 14;
    var wind = {};
    var mostAp = ["", 1];
    for (var _i = 0, _a = input.slice(0, windL).split(""); _i < _a.length; _i++) {
        var c = _a[_i];
        if (!(c in wind)) {
            wind[c] = 0;
        }
        wind[c] += 1;
        if (wind[c] > mostAp[1]) {
            mostAp[0] = c;
            mostAp[1] = wind[c];
        }
    }
    function solution() {
        var l = 0;
        var r = l + windL - 1;
        while (r < input.length) {
            if (mostAp[1] === 1) {
                return r + 1;
            }
            wind[input[l]] -= 1;
            l += 1;
            r += 1;
            if (!(input[r] in wind)) {
                wind[input[r]] = 0;
            }
            wind[input[r]] += 1;
            mostAp[1] = wind[mostAp[0]];
            for (var _i = 0, _a = input.slice(l, r + 1).split(""); _i < _a.length; _i++) {
                var c = _a[_i];
                if (wind[c] > mostAp[1]) {
                    mostAp[0] = c;
                    mostAp[1] = wind[c];
                }
            }
        }
        return -1;
    }
    console.log(solution());
});
