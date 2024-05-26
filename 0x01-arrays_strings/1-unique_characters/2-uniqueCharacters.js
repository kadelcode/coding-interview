function hasUniqueCharacters (string) {
  if (string.length > 128) {
    return false;
  }
  for (let i = 0; i < string.length; i++) {
    for (let j = i + 1; j < string.length; j++) {
      if (string[i] === string[j]) {
        return false;
      }
    }
  }
  return true;
}

// Test function
console.log(hasUniqueCharacters('great')); // true
console.log(hasUniqueCharacters('cool')); // false
