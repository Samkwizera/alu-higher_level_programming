#!/usr/bin/node

const args = process.argv.slice(2);
const arg = args[0];

const number = parseInt(arg, 10);

if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
