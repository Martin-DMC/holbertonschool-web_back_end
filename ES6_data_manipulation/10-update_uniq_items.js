export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Error');
  }

  for (const [item, quantity] of map.entries()) {
    if (quantity === 1) {
      map.set(item, 100)
    }
  }
}
