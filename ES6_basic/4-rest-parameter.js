export default function returnHowManyArguments(...args) {
  let cantidad = 0;
  for (const arg of args) {
    if (arg) {
      cantidad += 1;
    }
  }
  return cantidad;
}
