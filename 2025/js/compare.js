function comp(array1, array2) {
  if (Array.isArray(array1) && Array.isArray(array2)) {
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of
    for (let element of array1) {
      let index = array2.indexOf(element * element);
      if (index !== -1) {
        //usage:
        // array.splice(start, deleteCount, item1, item2, ...)
        array2.splice(index, 1);
      } else {
        return false;
      }
    }
    return true;
  } else {
    return false;
  }
}

let a1 = [121, 144, 19, 161, 19, 144, 19, 11];
let a2 = [
  11 * 11,
  121 * 121,
  144 * 144,
  19 * 19,
  161 * 161,
  19 * 19,
  144 * 144,
  19 * 19,
];
console.log(comp(a1, a2)); // true
console.log(comp([], [])); // true
console.log(comp([], null)); //false


