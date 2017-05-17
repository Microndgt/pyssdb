pyssdb_customized
=================

这是一个定制版的ssdb Python客户端, fork自[https://github.com/ifduyue/pyssdb](https://github.com/ifduyue/pyssdb), 增加了以下功能:

1. 增加了密码验证,不需要每次发请求时候 auth
2. 增加了返回数据直接decode至utf-8格式
3. 命令行ssdb数据库管理工具

使用
---

1. ssdb客户端

下载到本地,放到本地项目中,在其他模块中引入即可

```
from pyssdb_customized import pyssdb
ssdb = pyssdb.Client(host='localhost', port=8888, password='')
ssdb.hlist('0', 'z', 999)
```

如果认证成功,将会返回正常数据,如果认证失败,将会返回`'error:invalid password'`

2. 管理工具

###Usage

```
sudo python ssdb_tools.py --help
Usage: ssdb_tools.py [OPTIONS]

Options:
  -h, --host TEXT      host of ssdb
  -p, --port INTEGER   port of ssdb
  -P, --password TEXT  password of ssdb
  -c, --clear TEXT     clear names of hashmap. -c tdx -c robot
  -f, --flush
  --help               Show this message and exit.
```

`-c`可以多次指定,删除hashmap中以这个字符串开始的所有name

`-f`清空数据库