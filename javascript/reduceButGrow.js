function grow(x){
  let ans = 1;
  for (let i of x){
    ans *= i;
  }
  return ans;
}