import click
import click_log
import pkg_resources
#path = pkg_resources.resource_filename('package_folder', 'lib/java.jar')

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
click_log.basic_config(logger)

@click.group()
@click_log.simple_verbosity_option(logger)
@click.option('--verbose', default=False, is_flag=True)
def cli(verbose):
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.ERROR)

@cli.command("name_of_the_command")
def main():
    pass

