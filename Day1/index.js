const fs = require('fs')

let raw = fs.readFileSync("values.txt").toString();
let clean = raw.split("\r\n")
console.log(clean)

//Part 1

function FuncPartI(list){
    let total = 0;
    for(let i = 1; i < clean.length; i++){
        (clean[i]> clean[i-1]) ? total++ : total
    }
    return total
}

console.log(FuncPartI(clean))