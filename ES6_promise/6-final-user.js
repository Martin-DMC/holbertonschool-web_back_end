import signUpUser from "./4-user-promise";
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);

  return Promise.allSettled([userPromise, photoPromise]).then((results) => {
    return results.map((result) => {
      if (result.status === 'rejected') {
        return {
          status: 'rejected',
          value: `Error: ${fileName} cannot be processed`
        };
      }
      return result;
    });
  });
}