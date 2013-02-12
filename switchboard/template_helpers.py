"""
switchboard.template_helpers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010 Dice.
:license: Apache License 2.0, see LICENSE for more details.
"""

from . import operator

def is_active(key, *args):
    """
    Custom jinja test to make checking switches super easy:

    {% if 'my_switch' is active %}
    ...
    {% endif %}

    As with the operator.is_active() method, arbitrary objects may be
    passed in for use in testing whether the switch is active:

    {% if 'my_switch' is active(request, user) %}
    ...
    {% endif %}

    To setup the test in your jinja environment, update the tests
    dict on the environment:

    from switchboard.template_helpers import is_active
    environment.tests['active'] = is_active
    """
    return operator.is_active(key, *args)

