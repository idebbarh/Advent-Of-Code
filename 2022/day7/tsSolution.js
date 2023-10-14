var readFile = require("fs").readFile;

var Stack = /** @class */ (function () {
  function Stack() {}
  Stack.prototype.constructer = function () {
    this.items = [];
  };
  Stack.prototype.size = function () {
    return this.size.length;
  };
  Stack.prototype.push = function (value) {
    this.items.push(value);
  };
  Stack.prototype.pop = function () {
    if (this.size() > 0) {
      return this.items.pop();
    }
    return null;
  };
  return Stack;
})();
var stack = new Stack();
readFile("./input.txt", "utf8", function (err, data) {
  if (err) {
    return;
  }
  var input = data.split("\n");
  var res;
  var maxSize = 100000;
  for (var _i = 0, input_1 = input; _i < input_1.length; _i++) {
    var l = input_1[_i];
    if (l === "") {
      continue;
    }
    var line = l.split(" ");
    if (line[0] === "dir" || line[1] === "ls") {
      continue;
    }
    if (line[0] == "$") {
      if (line[2] === "..") {
        var poped = stack.pop();
        if (poped[1] <= maxSize) {
          res += poped[1];
        }
        stack.items[stack.size() - 1][1] += poped[1];
        continue;
      }
      stack.push([line[2], 0]);
    } else {
      stack[stack.size() - 1][1] += parseInt(line[0]);
    }
  }
  console.log(res);
});
