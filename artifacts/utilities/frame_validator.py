import click
import json
import yaml
import os

def validate_frame_structure(data):
    """
    Validates that the data represents a basic frame structure (a dictionary).
    """
    if not isinstance(data, dict):
        return False, "Root structure is not a dictionary (frame)."
    return True, "Valid frame structure."

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
def main(file_path):
    """
    A Click-based CLI tool for validating JSON/YAML frame structures.
    """
    click.echo(f"Validating file: {file_path}")

    file_extension = os.path.splitext(file_path)[1].lower()

    try:
        with open(file_path, 'r') as f:
            if file_extension == '.json':
                try:
                    data = json.load(f)
                    click.echo("File identified as JSON.")
                except json.JSONDecodeError:
                    click.secho("Error: Invalid JSON format.", fg='red')
                    return
            elif file_extension in ['.yaml', '.yml']:
                try:
                    data = yaml.safe_load(f)
                    click.echo("File identified as YAML.")
                except yaml.YAMLError:
                    click.secho("Error: Invalid YAML format.", fg='red')
                    return
            else:
                click.secho(f"Error: Unsupported file type '{file_extension}'. Please use .json, .yaml, or .yml.", fg='red')
                return

        is_valid, message = validate_frame_structure(data)

        if is_valid:
            click.secho(f"Validation successful: {message}", fg='green')
        else:
            click.secho(f"Validation failed: {message}", fg='red')

    except Exception as e:
        click.secho(f"An unexpected error occurred: {e}", fg='red')

if __name__ == '__main__':
    main()