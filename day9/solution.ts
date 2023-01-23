import * as fs from "fs";

let moves = fs.readFileSync("./input.txt", "utf-8").split("\n");
let res: Set<string> = new Set();

function manhattanDistance(p1: number[], p2: number[]): number {
  let [x1, y1] = p1;
  let [x2, y2] = p2;
  return Math.sqrt(Math.abs(x1 - x2) ** 2 + Math.abs(y1 - y2) ** 2);
}

function isTwoPointsAdj(p1: number[], p2: number[]): boolean {
  return manhattanDistance(p1, p2) <= Math.SQRT2;
}

function closestPoint(
  cp: [number, number],
  points: [number, number][]
): [number, number] {
  let minDis: number = Infinity;
  let closestP: [number, number] = [0, 0];
  for (let p of points) {
    const curDis = manhattanDistance(cp, p);
    if (curDis < minDis) {
      minDis = curDis;
      closestP = p;
    }
  }
  return closestP;
}

let knotsPos: [number, number][] = [
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

const DIRECTIONS = {
  U: [0, 1],
  D: [0, -1],
  L: [1, -1],
  R: [1, 1],
};
function moveMeBabby(d: string, one: number, two: number) {
  if (one >= knotsPos.length - 1) {
    return;
  }
  if (one === 0) {
    knotsPos[one][DIRECTIONS[d][0]] += DIRECTIONS[d][1];
  }
  if (!isTwoPointsAdj(knotsPos[one], knotsPos[two])) {
    let listOfPoints: [number, number][] = [];
    for (let d of [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
      [1, 1],
      [1, -1],
      [-1, 1],
      [-1, -1],
    ]) {
      let [v1, v2] = d;
      listOfPoints.push([knotsPos[two][0] + v1, knotsPos[two][1] + v2]);
    }
    knotsPos[two] = closestPoint(knotsPos[one], listOfPoints);
    moveMeBabby(d, one + 1, two + 1);
  }
}
function main() {
  for (let move of moves) {
    if (move === "") {
      continue;
    }
    let [d, n] = move.split(" ");
    for (let i = 0; i < parseInt(n); i++) {
      moveMeBabby(d, 0, 1);
      res.add(JSON.stringify(knotsPos[knotsPos.length - 1]));
    }
  }
  console.log(res.size);
}
main();
