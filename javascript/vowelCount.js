function getCount(str) {
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  let count = 0;
  let letters = str.split('');

  for (let i of letters){
    if (vowels.includes(i)) count += 1;
  }

  return count
}

console.log('count', getCount("abracadabra"))