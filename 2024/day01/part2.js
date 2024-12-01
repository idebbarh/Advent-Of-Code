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

  let res = 0;

  const cache = {};

  for (let l of leftIds) {
    if (cache.hasOwnProperty(l)) {
      res += cache[l];
      continue;
    }

    let c = 0;

    for (let r of rightIds) {
      if (l === r) c++;
    }

    const m = l * c;

    cache[l] = m;

    res += m;
  }

  console.log("result: ", res);
});
