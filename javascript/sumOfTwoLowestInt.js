function sumTwoSmallestNumbers(numbers) {
  let arr = numbers.sort((a,b) => a - b)
  return arr[0] + arr[1]
}

console.log(sumTwoSmallestNumbers([5,4,3,2,1]))