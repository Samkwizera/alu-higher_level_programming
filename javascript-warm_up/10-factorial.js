#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0], 10);

const factorial = (n) => {
    if (n <= 1 || isNaN(n)) {
        return 1;
    }
    return n * factorial(n - 1);
};

console.log(factorial(num));

