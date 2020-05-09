"""Create new Avanza Stock Sensors."""

import click
import csv
from string import Template
import jinja2

TEMPLATE_FILE = "avanza_stock.yaml.template"
TEMPLATE_PAGE_FILE = "avanza_stock.page.yaml.template"
OUTPUT_FILE_PATH = "../../dwains-theme/addons/more_page/finance/page.yaml"

@click.command()
# @click.argument('name', type=click.STRING)
# @click.argument('id', type=click.INT)
# def cli(name, id):
def cli():
    """Create new Avanza Stock Sensors.

    NAME: The name of the stock.\n
    ID: The Avanza id of the stock. Obtainable via the URL.
    """

    stocks = []
    with open('stocks.csv', newline='') as csvfile:
        reader = csv.DictReader(filter(lambda row: row[0]!='#', csvfile))
        for row in reader: 

            filein = open( TEMPLATE_FILE )
            template = Template( filein.read() )
            name = row['name']
            stocks.append(name)
            result = template.safe_substitute(name=name,id=row['id'])
            filename = f"avanza_stock_{name}.yaml"
            with open(filename, "w") as f:
                f.write(result)

    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(TEMPLATE_PAGE_FILE)
    outputText = template.render(stocks=stocks)  # this is where to put args to the template renderer

    with open(OUTPUT_FILE_PATH, "w") as f:
        f.write(outputText)


if __name__ == '__main__':
    cli()