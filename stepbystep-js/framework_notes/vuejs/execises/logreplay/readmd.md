
notes:
- 	url = https://github.com/adamlundrigan/nodejs-logreplay.git
- usage

```sh
node replay.js <file>
```

1. Install Node.js and the following packages from npm:
 * lazy
 * konphyg

2. Clone this repository onto the server you wish to launch your load test requests from


Copy the provided configuration file `config/example.json.dist` to `config/<something>.json` and edit
 * `source`: Full path to the access log you want to replay
 * `speedupFactor`: Speed at which log is replayed (ie: 2 = twice normal speed) 
 * `target`: Specifies the target of the load testing
     * `host`: hostname of target machine
     * `port`: target port (for SSL, only 443 is supported)

4. Run the profile you created (the `<something>` you chose in #3)

       ```node replay.js <something>```