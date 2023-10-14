import * as fs from "fs";

interface StackT {
  items: [string, number][];
  push: (value: [string, number]) => void;
  size: () => number;
  pop: () => [string, number] | null | undefined;
}

class Stack implements StackT {
  items: [string, number][];
  constructer() {
    this.items = [];
  }
  size() {
    return this.size.length;
  }
  push(value: [string, number]) {
    this.items.push(value);
  }

  pop() {
    if (this.size() > 0) {
      return this.items.pop();
    }
    return null;
  }
}

const stack = new Stack();
readFile("./input.txt", "utf8", (err: any, data: string) => {
  if (err) {
    return;
  }
  let input: string[] = data.split("\n");
  let res: number = 0;
  let maxSize: number = 100000;
  for (let l of input) {
    if (l === "") {
      continue;
    }
    let line: string[] = l.split(" ");
    if (line[0] === "dir" || line[1] === "ls") {
      continue;
    }
    if (line[0] == "$") {
      if (line[2] === "..") {
        let poped = stack.pop();
        if (poped && poped[1] <= maxSize) {
          res += poped[1];
        }
        if (poped) {
          stack.items[stack.size() - 1][1] += poped[1];
        }
        continue;
      }
      stack.push([line[2], 0]);
    } else {
      stack[stack.size() - 1][1] += parseInt(line[0]);
    }
  }
  console.log(res);
});
