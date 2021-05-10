import unittest

from flask.cli import FlaskGroup
import coverage as coverage


from project import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)

coverage = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
coverage.start()


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
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        coverage.stop()
        coverage.save()
        print('Coverage Summary:')
        coverage.report()
        coverage.html_report()
        coverage.erase()
        return 0
    return 1


if __name__ == '__main__':
    cli()
