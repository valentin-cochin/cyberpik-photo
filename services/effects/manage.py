import unittest

from flask.cli import FlaskGroup
import coverage as coverage


from project import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def test():
    """ Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    cover = coverage.coverage()
    cover.start()
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        cover.stop()
        cover.save()
        print('Coverage Summary:')
        cover.report()
        cover.html_report()
        cover.erase()
        return 0
    return 1


if __name__ == '__main__':
    cli()
