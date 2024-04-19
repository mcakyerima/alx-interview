# ALX 0x06-starwars_api Challenge
=============================

## Description
-----------
This challenge involves creating a Node.js script that retrieves and displays the names of characters from a given Star Wars film using the SWAPI API.

## Script Explanation
--------------------
The script, `0-starwars_characters.js`, takes a film ID as a command-line argument and performs the following tasks:

1. Sends a GET request to the SWAPI API to retrieve the film data.
2. Extracts the list of character URLs from the film data.
3. Recursively sends GET requests to each character URL to retrieve the character data.
4. Logs the name of each character to the console.

## Usage
-----
To run the script, navigate to the `0x06-starwars_api` directory and execute the following command:
```bash

./0-starwars_characters.js <film_id>

Replace <film_id> with the ID of the Star Wars film you want to retrieve characters for.
Note
----
This script assumes you have Node.js installed on your system. If you don't have Node.js installed, you can download and install it from the official Node.js website.

Author
-------
Mohammed Kaka

