//NodeJS script for automatically converting list.txt to list.json
//To run use "node txt_to_json.js"
//Will convert every line of the TXT file into its own entry in the array in the JSON file
//Does not require installation of any packages. Filesystem and readline come with NodeJS by default.

const fs = require('fs')
const readline = require('readline');
(async () => {
    console.log('Started.')
    const fileStream = fs.createReadStream('list.txt');
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });
    const out = [];
    rl.on('line', async (line) => {
        out.push(line)
    })
    rl.on('close', () => {
        fs.writeFile('list.json', JSON.stringify(out), (err) => {
            if (err) return console.error(err)
            else console.log('Completed.')
        })
    })
})();