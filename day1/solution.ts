import * as fs from "fs";
let input: string[];
fs.readFile("./input.txt", "utf8", (err, data) => {
  if (err) {
    return;
  }
  input = data.split("\n");
  let res: number[] = [-Infinity, -Infinity, -Infinity];
  let curT: number = 0;
  for (let n of input) {
    if (n === "") {
      let v1 = res[0];
      let v2 = res[1];
      let v3 = res[2];
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
