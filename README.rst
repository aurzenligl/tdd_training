Continuous Integration status can be found here:

.. image:: https://travis-ci.org/aurzenligl/tdd_training.svg?branch=master
    :target: https://travis-ci.org/aurzenligl/tdd_training
    :alt: Travis-CI Build Status

You can test whole project in all configurations by running tox::

    $ pip install tox
    $ tox

You can test project with chosen interpreter by running pytest from virtualenv::

    $ . init-tox-env
    $ pytest
