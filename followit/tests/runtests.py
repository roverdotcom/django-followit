import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'followit.tests.settings'
from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['tests.FollowerTests',])
if failures:
    sys.exit(failures)
