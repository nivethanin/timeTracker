import click

@click.group
def cli():
    pass

@cli.command()
def list():
    data = open("logs.txt","r")
    lines = data.read()
    print(lines)
    data.close()

@cli.command()
def total():
    data = open("logs.txt","r")
    w = data.read()
    s = w.split(',')
    total = 0

    for i in s:
        if i:
            total += int(i)

    print(total)


   
@cli.command()
@click.option('-subtract')
@click.argument('add')
def add(add, subtract):
    """Simple function to add to the time to the time file"""
    data = open("logs.txt","a")
    if subtract:
        data.write("-"+ add +",")
    else:
        data.write(add +",")
    data.close()


if __name__ == '__main__':
    cli()