export default function divideFunction(numerator, denominator) {
  if (denominator <= 0) {
    throw new Error('cannot divide by 0');
  }
  if (typeof denominator !== 'number' || typeof numerator !== 'number') {
    throw new Error('parameters must be a number');
  }

  const result = numerator / denominator;

  return result;
}
