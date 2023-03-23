function countSheeps(arrayOfSheep) {
  let count = 0;
  for (let i of arrayOfSheep){
    if (i === true){
      count+=1;
    }
  }
  return count
}
