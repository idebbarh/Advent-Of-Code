"use strict";
exports.__esModule = true;
var fs = require("fs");
var input;
fs.readFile("./input.txt", "utf8", function (err, data) {
  if (err) {
    return;
  }
  input = data.split("\n");
  var res = [-Infinity, -Infinity, -Infinity];
  var curT = 0;
  for (var _i = 0, input_1 = input; _i < input_1.length; _i++) {
    var n = input_1[_i];
    if (n === "") {
      var v1 = res[0];
      var v2 = res[1];
      var v3 = res[2];
      if (curT > res[0]) {
        res[0] = curT;
        res[1] = v1;
        res[2] = v2;
      } else if (curT > res[1]) {
        res[1] = curT;
        res[2] = v2;
      } else {
        res[2] = Math.max(v3, curT);
      }
      curT = 0;
      continue;
    }
    curT += parseInt(n);
  }
  console.log(res[0] + res[1] + res[2]);
});
