from os import path
import time

import bolt

import bolt_flask
import behave_restful.bolt_behave_restful as br

bolt.register_module_tasks(bolt_flask)
bolt.register_module_tasks(br)

PROJECT_ROOT = path.abspath(path.dirname(__file__))
SRC_DIR = path.join(PROJECT_ROOT, 'battleship')
TESTS_DIR = path.join(PROJECT_ROOT, 'tests')
FEATURES_DIR = path.join(PROJECT_ROOT, 'features')

bolt.register_task('ut', ['delete-pyc', 'delete-pyc.from-tests', 'nose'])
bolt.register_task('ct', ['conttest'])
bolt.register_task('ft', ['delete-pyc', 'start-flask', 'wait', 'behave-restful'])


def wait(config, **_ignored):
    seconds = config.get('seconds', 0)
    time.sleep(seconds)

bolt.register_task('wait', wait)


config = {
    'delete-pyc': {
        'sourcedir': SRC_DIR,
        'recursive': True,
        'from-tests': {
            'sourcedir': TESTS_DIR,
        }
    },
    'nose': {
        'directory': TESTS_DIR,
    },
    'conttest': {
        'task': 'ut',
        'directory': PROJECT_ROOT
    },
    'start-flask': {
        'startup-script': path.join(PROJECT_ROOT, 'app.py')
    },
    'behave-restful': {
        'directory': FEATURES_DIR,
        'definition': 'local',
    },
    'wait': {
        'seconds': 2,
    }
}
