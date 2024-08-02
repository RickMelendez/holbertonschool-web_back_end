export default function getFullResponseFromAPI() {
  return new Promise((resolve, reject) => {

    const success = true;

    if (success) {
      resolve({
        status: 200,
        body: 'Success',
      });
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
  