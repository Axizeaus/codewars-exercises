// https://www.codewars.com/kata/515e271a311df0350d00000f/train/javascript

function squareSum(numbers){
  return numbers.map(x => x ** 2).reduce((x,y) => x + y, 0);
}

console.log(squareSum([1,2]));