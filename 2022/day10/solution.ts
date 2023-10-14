import * as fs from "fs";

let input: string = fs.readAsync("./input.txt", "utf-8").split("\n");

const cyclesToKnow: number[] = [20, 60, 100, 140, 180, 220];
let res: number[] = [];
let xVal: number = 1;
let curCycle: number = 0;

function isThisIsTheMoment(): void {
  if (cyclesToKnow.includes(curCycle)) {
    res.push(xVal * curCycle);
  }
}

for (let step of input) {
  if (step === "") {
    continue;
  }
  if (step === "noop") {
    curCycle += 1;
    isThisIsTheMoment();
  } else {
    let [, n] = step.split(" ");
    curCycle += 1;
    isThisIsTheMoment();
    curCycle += 1;
    isThisIsTheMoment();
    xVal += parseInt(n);
  }
}
