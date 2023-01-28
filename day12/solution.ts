import * as fs from "fs";
let grid: string[][] = fs
  .readFileSync("input.txt", "utf8")
  .split("\n")
  .filter((row: string): boolean => row !== "")
  .map((row: string): string[] => row.split(""));

function getNextLetter(letter: string): string {
  return String.fromCharCode(letter.charCodeAt(0) + 1);
}
function charCode(letter: string): number {
  return letter.charCodeAt(0);
}
function manhattanDistance(a: TNode, b: TNode): number {
  return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
}
function nodeWithLowestFCost(openSet: TNode[]): TNode {
  let lowestFCost = Infinity;
  let lowestFCostNode: TNode = openSet[0];
  for (let node of openSet) {
    if (node.fCost < lowestFCost) {
      lowestFCost = node.fCost;
      lowestFCostNode = node;
    }
  }
  return lowestFCostNode;
}
function calcFCost(node: TNode): number {
  return node.gCost + node.hCost;
}
interface TNode {
  value: string;
  id: [number, number];
  x: number;
  y: number;
  parent: TNode | undefined | null;
  gCost: number;
  hCost: number;
  fCost: number;
  getNeighbors: () => TNode[];
  getValidNeighbors: () => TNode[];
}
class Node implements TNode {
  constructor(
    public value: string,
    public id: [number, number],
    public x: number,
    public y: number,
    public parent: TNode | undefined | null,
    public gCost: number,
    public hCost: number,
    public fCost: number
  ) {}
  getNeighbors(): TNode[] {
    let neighbors: TNode[] = [];
    let x = this.x;
    let y = this.y;
    if (x > 0)
      neighbors.push(
        new Node(
          grid[x - 1][y],
          [x - 1, y],
          x - 1,
          y,
          undefined,
          Infinity,
          Infinity,
          Infinity
        )
      );
    if (x < grid.length - 1)
      neighbors.push(
        new Node(
          grid[x + 1][y],
          [x + 1, y],
          x + 1,
          y,
          undefined,
          Infinity,
          Infinity,
          Infinity
        )
      );
    if (y > 0)
      neighbors.push(
        new Node(
          grid[x][y - 1],
          [x, y - 1],
          x,
          y - 1,
          undefined,
          Infinity,
          Infinity,
          Infinity
        )
      );
    if (y < grid[0].length - 1)
      neighbors.push(
        new Node(
          grid[x][y + 1],
          [x, y + 1],
          x,
          y + 1,
          undefined,
          Infinity,
          Infinity,
          Infinity
        )
      );
    return neighbors;
  }
  getValidNeighbors(): TNode[] {
    let neighbors = this.getNeighbors();
    return neighbors.filter(
      (neighbor) =>
        neighbor.value === getNextLetter(this.value) ||
        charCode(neighbor.value) <= charCode(this.value)
    );
  }
}
const startNode = new Node("a", [0, 0], 0, 0, null, 0, Infinity, Infinity);
const endNode = new Node(
  "z",
  [0, 0],
  0,
  0,
  undefined,
  Infinity,
  Infinity,
  Infinity
);
for (let i = 0; i < grid.length; i++) {
  for (let j = 0; j < grid[0].length; j++) {
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
function aStart(): void {
  let openList: TNode[] = [];
  let openSet = new Set<string>();
  const closedSet = new Set<string>();

  openList.push(startNode);
  openSet.add(JSON.stringify(startNode.id));

  while (openList.length > 0) {
    let current = nodeWithLowestFCost(openList);
    if (current.id === endNode.id) {
      endNode.parent = current.parent;
    }
    openList = openList.filter((item) => item.id !== current.id);
    openSet.delete(JSON.stringify(current.id));

    for (let neighbor of current.getNeighbors()) {
      if (closedSet.has(JSON.stringify(neighbor.id))) {
        continue;
      }
      const newCost = current.gCost + manhattanDistance(current, neighbor);
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
  }
}
aStart();

function calcSteps(): number {
  let current: TNode | undefined | null = endNode.parent;
  let steps: number = 0;
  while (current !== null) {
    steps++;
    current = current?.parent;
  }
  return steps;
}

console.log(calcSteps());
