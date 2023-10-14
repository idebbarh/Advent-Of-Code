"use strict";
exports.__esModule = true;
var fs = require("fs");
var moves = fs.readFileSync("./input.txt", "utf-8").split("\n");
function manhattanDistance(p1, p2) {
    var x1 = p1[0], y1 = p1[1];
    var x2 = p2[0], y2 = p2[1];
    return Math.sqrt(Math.pow(Math.abs(x1 - x2), 2) + Math.pow(Math.abs(y1 - y2), 2));
}
function isTwoPointsAdj(p1, p2) {
    return manhattanDistance(p1, p2) <= Math.SQRT2;
}
function closestPoint(cp, points) {
    var minDis = Infinity;
    var closestP = [0, 0];
    for (var _i = 0, points_1 = points; _i < points_1.length; _i++) {
        var p = points_1[_i];
        var curDis = manhattanDistance(cp, p);
        if (curDis < minDis) {
            minDis = curDis;
            closestP = p;
        }
    }
    return closestP;
}
var knotsPos = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
];
var DIRECTIONS = {
    U: [0, 1],
    D: [0, -1],
    L: [1, -1],
    R: [1, 1]
};
function moveMeBabby(d, one, two) {
    if (one >= knotsPos.length - 1) {
        return;
    }
    if (one === 0) {
        knotsPos[one][DIRECTIONS[d][0]] += DIRECTIONS[d][1];
    }
    if (!isTwoPointsAdj(knotsPos[one], knotsPos[two])) {
        var listOfPoints = [];
        for (var _i = 0, _a = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1],
        ]; _i < _a.length; _i++) {
            var d_1 = _a[_i];
            var v1 = d_1[0], v2 = d_1[1];
            listOfPoints.push([knotsPos[two][0] + v1, knotsPos[two][1] + v2]);
        }
        knotsPos[two] = closestPoint(knotsPos[one], listOfPoints);
        moveMeBabby(d, one + 1, two + 1);
    }
}
var res = new Set();
function main() {
    for (var _i = 0, moves_1 = moves; _i < moves_1.length; _i++) {
        var move = moves_1[_i];
        if (move === "") {
            continue;
        }
        var _a = move.split(" "), d = _a[0], n = _a[1];
        for (var i = 0; i < parseInt(n); i++) {
            moveMeBabby(d, 0, 1);
            res.add(JSON.stringify(knotsPos[knotsPos.length - 1]));
        }
    }
    console.log(res.size);
}
main();
