export default async function getResponseFromAPI() {
    const response = await fetch('https://www.google.com');
    return response;
}
