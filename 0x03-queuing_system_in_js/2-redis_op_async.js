import {createClient, print} from './redis_client';
import { promisify } from 'util'; 

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server')
})
client.on('error', (error) => {
    console.log('Redis client not connected to the server: ${error}');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

const get = promisify(client.get).bind(client)

async function displaySchoolValue(schoolName) {
    const response = await client.get(schoolName).catch((error) => {
    // client.get(schoolName, (error, result) => {
        if (error) {
            console.log(error);
            throw error;
        }
    });
    console.log(response);
    }

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
