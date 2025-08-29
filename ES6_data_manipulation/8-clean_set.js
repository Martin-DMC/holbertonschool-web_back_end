export default function cleanSet(set, starString) {
  if (starString === '') {
    return '';
  }

  const result = [];

  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(starString)) {
      const cleanedValue = value.substring(starString.length);
      result.push(cleanedValue);
    }
  }

  return result.join('-');
}
