function openOrSenior(data) {
  return data.map((e) => {
    if (e[0] >= 55 && e[1] > 7) {
      return "Senior";
    } else {
      return "Open";
    }
  });
}

console.log(
  openOrSenior([
    [18, 20],
    [45, 2],
    [61, 12],
    [37, 6],
    [21, 21],
    [78, 9],
  ])
); // ["Open", "Open", "Senior", "Open", "Open", "Senior"]]
