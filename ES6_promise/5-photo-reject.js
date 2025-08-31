export default function uploadPhoto(fileName) {
  return new Promise((resolve, reject) => {
    if (fileName) {
        reject(new Error(`${fileName} cannot be processed`));
    }else {
        resolve({status: 200, body: 'exito'});
    }
  })
}
