// https://www.codewars.com/kata/57eaec5608fed543d6000021/train/javascript

function divCon(x) {
  let numArray = [];
  let strArray = [];
  for (let i of x){
    if (Number.isInteger(i)){
      numArray.push(i)
    } else {
      strArray.push(Number.parseInt(i))
    }
  }

  let num = numArray.reduce((accumulator, value) => accumulator + value, 0);
  let str = strArray.reduce((accumulator, value) => accumulator + value, 0);

  return num - str;
}
