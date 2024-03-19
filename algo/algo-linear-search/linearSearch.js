function linearSearch(searchTerm, arr) {
  /*
  loops through the array checking to see if element = searchterm
  if yes, return its index
  if no, do nothing
  at end, if no match, returns undefined
  */
  for (let i = 0; i < arr.length; i++)
    if (searchTerm === arr[i]) {
      return i;
    } else {
    }
    return undefined;
}

function globalLinearSearch(searchTerm, arr) {
    /*
  loops through the array checking to see if element = searchterm
  if yes, add that index to indexArr
  if no, do nothing
  */
  let indexArr = []
  for (let i = 0; i < arr.length; i++)
    if (searchTerm === arr[i]) {
      indexArr.push(i);
    } else {
    }

  /*
  if no indexes were added tot he empty array, return undefined
  if they were, return the array
  */
    if (indexArr.length === 0) {
      return undefined;
    } else {
      return indexArr;
    }
}

module.exports = { linearSearch, globalLinearSearch };
