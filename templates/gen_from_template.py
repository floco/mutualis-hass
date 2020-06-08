"""Create All Links."""

import click
import csv
from string import Template
import jinja2
import os



@click.command()
@click.option('--source-csv', required=True, type=str)
@click.option('--template', required=True, type=str)
@click.option('--output', required=True, type=str)

def cli(source_csv,template,output):

    click.echo(f"Generating {output} from {template} ...") 

    SOURCE_PATH = "./templates"
    CSV_FILE = source_csv
    TEMPLATE_FILE = template
    OUTPUT_FILE_PATH = output

    csv_file = os.path.join(SOURCE_PATH, CSV_FILE)

    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(filter(lambda row: row[0]!='#', csvfile))

        templateLoader = jinja2.FileSystemLoader(searchpath=SOURCE_PATH)
        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template(TEMPLATE_FILE)
        outputText = template.render(items=reader)

        with open(OUTPUT_FILE_PATH, "w") as f:
            f.write(outputText)
        
    click.echo(f"Created {output}") 


if __name__ == '__main__':
    cli()