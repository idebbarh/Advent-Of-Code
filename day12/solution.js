"use strict";
exports.__esModule = true;
var fs = require("fs");
var grid = fs
    .readFileSync("input.txt", "utf8")
    .split("\n")
    .filter(function (row) { return row !== ""; })
    .map(function (row) { return row.split(""); });
function getNextLetter(letter) {
    return String.fromCharCode(letter.charCodeAt(0) + 1);
}
function charCode(letter) {
    return letter.charCodeAt(0);
}
function manhattanDistance(a, b) {
    return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
}
function nodeWithLowestFCost(openSet) {
    var lowestFCost = Infinity;
    var lowestFCostNode = openSet[0];
    for (var _i = 0, openSet_1 = openSet; _i < openSet_1.length; _i++) {
        var node = openSet_1[_i];
        if (node.fCost < lowestFCost) {
            lowestFCost = node.fCost;
            lowestFCostNode = node;
        }
    }
    return lowestFCostNode;
}
function calcFCost(node) {
    return node.gCost + node.hCost;
}
var Node = /** @class */ (function () {
    function Node(value, id, x, y, parent, gCost, hCost, fCost) {
        this.value = value;
        this.id = id;
        this.x = x;
        this.y = y;
        this.parent = parent;
        this.gCost = gCost;
        this.hCost = hCost;
        this.fCost = fCost;
    }
    Node.prototype.getNeighbors = function () {
        var neighbors = [];
        var x = this.x;
        var y = this.y;
        if (x > 0)
            neighbors.push(new Node(grid[x - 1][y], [x - 1, y], x - 1, y, undefined, Infinity, Infinity, Infinity));
        if (x < grid.length - 1)
            neighbors.push(new Node(grid[x + 1][y], [x + 1, y], x + 1, y, undefined, Infinity, Infinity, Infinity));
        if (y > 0)
            neighbors.push(new Node(grid[x][y - 1], [x, y - 1], x, y - 1, undefined, Infinity, Infinity, Infinity));
        if (y < grid[0].length - 1)
            neighbors.push(new Node(grid[x][y + 1], [x, y + 1], x, y + 1, undefined, Infinity, Infinity, Infinity));
        return neighbors;
    };
    Node.prototype.getValidNeighbors = function () {
        var _this = this;
        var neighbors = this.getNeighbors();
        return neighbors.filter(function (neighbor) {
            return neighbor.value === getNextLetter(_this.value) ||
                charCode(neighbor.value) <= charCode(_this.value);
        });
    };
    return Node;
}());
var startNode = new Node("a", [0, 0], 0, 0, null, 0, Infinity, Infinity);
var endNode = new Node("z", [0, 0], 0, 0, undefined, Infinity, Infinity, Infinity);
for (var i = 0; i < grid.length; i++) {
    for (var j = 0; j < grid[0].length; j++) {
        if (grid[i][j] === "S") {
            grid[i][j] = "a";
            startNode.x = i;
            startNode.y = j;
        }
        if (grid[i][j] === "E") {
            grid[i][j] = "z";
            endNode.x = i;
            endNode.y = j;
        }
    }
}
function aStart() {
    var openList = [];
    var openSet = new Set();
    var closedSet = new Set();
    openList.push(startNode);
    openSet.add(JSON.stringify(startNode.id));
    var _loop_1 = function () {
        var current = nodeWithLowestFCost(openList);
        if (current.id === endNode.id) {
            endNode.parent = current.parent;
        }
        openList = openList.filter(function (item) { return item.id !== current.id; });
        openSet["delete"](JSON.stringify(current.id));
        for (var _i = 0, _a = current.getNeighbors(); _i < _a.length; _i++) {
            var neighbor = _a[_i];
            if (closedSet.has(JSON.stringify(neighbor.id))) {
                continue;
            }
            var newCost = current.gCost + manhattanDistance(current, neighbor);
            if (newCost < neighbor.gCost) {
                neighbor.parent = current;
                neighbor.gCost = newCost;
                neighbor.hCost = manhattanDistance(neighbor, endNode);
                neighbor.fCost = calcFCost(neighbor);
                if (!openSet.has(JSON.stringify(neighbor.id))) {
                    openSet.add(JSON.stringify(neighbor.id));
                    openList.push(neighbor);
                }
            }
        }
    };
    while (openList.length > 0) {
        _loop_1();
    }
}
aStart();
function calcSteps() {
    var current = endNode.parent;
    var steps = 0;
    while (current !== null) {
        steps++;
        current = current === null || current === void 0 ? void 0 : current.parent;
    }
    return steps;
}
console.log(calcSteps());
