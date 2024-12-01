const fs = require("fs");

fs.readFile("./real-input.txt", "utf8", (err, data) => {
  const lines = data.split("\n");
  const leftIds = [];
  const rightIds = [];
  lines
    .filter(Boolean)
    .map((line) => line.split("   ").map((n) => parseInt(n)))
    .forEach(([l, r]) => {
      leftIds.push(l);
      rightIds.push(r);
    });

  leftIds.sort();
  rightIds.sort();

  let res = 0;

  for (let i = 0; i < Math.min(leftIds.length, rightIds.length); i++) {
    const left = leftIds[i];
    const right = rightIds[i];

    res += Math.abs(left - right);
  }

  console.log("result: ", res);
});
