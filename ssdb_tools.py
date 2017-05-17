import click
import pyssdb


def clear_names(db, names):
    all_names = db.hlist('', '', 99999999)
    if not all_names:
        return
    for name in all_names:
        if name.startswith(names):
            db.hclear(name)


@click.command()
@click.option('-h', '--host', default='localhost', help='host of ssdb')
@click.option('-p', '--port', default=5003, help='port of ssdb')
@click.option('-P', '--password', default='', help='password of ssdb')
@click.option('-c', '--clear', multiple=True, help="clear names of hashmap. -c tdx -c robot")
@click.option('-f', '--flush', is_flag=True)
def ssdb_tool(host, port, password, clear, flush):
    db = pyssdb.Client(host=host, port=port, password=password)
    if flush:
        db.flushdb()
    if clear:
        clear_names(db, clear)

if __name__ == "__main__":
    ssdb_tool()
