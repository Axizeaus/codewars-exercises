function bubble_sort(arr){
  let unsorted_until_index = arr.length - 1
  let sorted = false 

  while (!sorted) {
    sorted = true;
    for (let i = 0; i < unsorted_until_index; i++) {
      if (arr[i] > arr[i + 1]) {
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        sorted = false
      }
      console.log(unsorted_until_index, arr)
    }
    unsorted_until_index -= 1;
  }
  return arr
}

console.log(bubble_sort([1,5,4,3,2,7,8,5,4,8]))