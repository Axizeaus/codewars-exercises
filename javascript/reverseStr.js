// https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/javascript

function digitize(n) {
  arr = Array.from(String(n), Number);
  return arr.reverse();
}

console.log(digitize(35231))