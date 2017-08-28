pyssdb_customized
=================

This is a customized pyssdb Client, forked from [https://github.com/ifduyue/pyssdb](https://github.com/ifduyue/pyssdb)

Features
--------

1. auth when getting new connection if password is provided
2. command send will transfer `numbers.Real` to utf-8 str, while `int` originally
3. data received will be transferred to utf-8 automatically
4. ssdb command tools

Usage
-----

1. SSDB Client

- install via pip

`pip install git+https://github.com/Microndgt/pyssdb_customized.git`

and then `from pyssdb import Client`

- install using py file

Copy pyssdb.py to your project, and import

```
from pyssdb import Client
ssdb = Client(host='localhost', port=8888, password='')
ssdb.hlist('0', 'z', 999)
```

2. Command tools

Usage

```
sudo python ssdb_tools.py --help
Usage: ssdb_tools.py [OPTIONS]

Options:
  -h, --host TEXT      host of ssdb
  -p, --port INTEGER   port of ssdb
  -P, --password TEXT  password of ssdb
  -c, --clear TEXT     clear names in hashmap. -c tdx -c robot
  -f, --flush
  --help               Show this message and exit.
```

`-c` delete specific names in hashmap

`-f` equal to flushdb