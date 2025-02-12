var number = function (array) {
  return array.map((e, index) => {
    return `${index + 1}: ${e}`;
  });
};

console.log(number(["a", "b", "c"])); // ["1: a", "2: b", "3: c"]
