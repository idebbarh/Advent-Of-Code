import * as fs from "fs";

interface Window {
  [key: string]: number;
}
fs.readFile("./input.txt", "utf8", (err: any, data: string) => {
  if (err) {
    return;
  }
  let input: string = data;
  let windL: number = 14;
  let wind: Window = {};
  let mostAp: [string, number] = ["", 1];
  for (let c of input.slice(0, windL).split("")) {
    if (!(c in wind)) {
      wind[c] = 0;
    }
    wind[c] += 1;
    if (wind[c] > mostAp[1]) {
      mostAp[0] = c;
      mostAp[1] = wind[c];
    }
  }
  function solution(): number {
    let l: number = 0;
    let r: number = l + windL - 1;
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
      for (let c of input.slice(l, r + 1).split("")) {
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
