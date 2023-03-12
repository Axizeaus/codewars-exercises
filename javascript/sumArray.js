// https://www.codewars.com/kata/53dc54212259ed3d4f00071c/javascript

function sum (numbers) {
  "use strict";
  return numbers.reduce(
    (accumulator, currentValue) => accumulator + currentValue, 0)
};

