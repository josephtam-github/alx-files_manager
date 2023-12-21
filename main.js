import redisClient from "./utils/redis";
import dbClient from "./utils/db";

const waitConnection = async (maxRetries = 10, retryInterval = 1000) => {
    for (let i = 0; i < maxRetries; i++) {
        await new Promise(resolve => setTimeout(resolve, retryInterval));
        if (dbClient.isAlive()) {
            return;
        }
    }
    throw new Error("Database connection not established within the specified time.");
};

const main = async () => {
    console.log(`Redis Client: ${redisClient.isAlive()}`);
    
    try {
        await waitConnection();
        console.log(`Database Client: ${dbClient.isAlive()}`);
        console.log(`Number of Users: ${await dbClient.nbUsers()}`);
        console.log(`Number of Files: ${await dbClient.nbFiles()}`);
    } catch (error) {
        console.error(error.message);
    }
};

main();
