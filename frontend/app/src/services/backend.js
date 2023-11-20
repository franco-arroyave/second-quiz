const baseUrl = 'http://172.18.0.4:5000';
const apiKey = '123';

export async function signup(username, email) {

    const response = await fetch(`${baseUrl}/user/jose`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email}),
    });
    const data = await response.json();
    return data;
}

export async function signin(username) {

    const response = await fetch(`${baseUrl}/user/${username}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    });
    const data = await response.json();
    return data;
}