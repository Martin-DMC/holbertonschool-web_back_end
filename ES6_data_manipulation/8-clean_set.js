export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') {
    return '';
  }

  const result = [];

  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      const cleanedValue = value.substring(startString.length);
      result.push(cleanedValue);
    }
  }

  return result.join('-');
}
