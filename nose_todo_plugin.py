"""This plugin installs a TODO warning class for the TodoWarningException.
When TodoWarningException is raised, the exception will be logged
in the todo attribute of the result, detailed reason will be logged in warning_list,
'W' or 'Warning' (verbose) will be output, and the exception will not be counted as an error
or failure.
"""
from nose.plugins.errorclass import ErrorClass, ErrorClassPlugin
from functools import wraps
import warnings

class TodoWarningException(Exception):
    """ Custom exception class for TodoWarningPlugin.
        Reason of using TodoWarningPlugin and exception are logged.
    """
    def __init__(self, reason, error):
        self.reason = reason
        self.error = error
    pass


class TodoWarningPlugin(ErrorClassPlugin):
    """ Installs a TODO warning class for the TodoWarningException.

    When TodoWarningException is raised, the exception will be logged
    in the todo attribute of the result, detailed reason will be logged in warning_list,
    'W' or 'Warning' (verbose) will be output, and the exception will not be counted as an error
    or failure.
    """
    name = 'todo'
    todo = ErrorClass(TodoWarningException, label='Warning', isfailure=False)
    warnings_list = []

    def formatError(self, test, err):
        """ Customize formatError plugin method.
            Add error details to warnings list to be used in finslize method.
        """
        self.warnings_list.append((err[1].reason, err[1].error))
        ec, ev, tb = err
        return (ec, ev, tb)

    def finalize(self, result):
        """ Customize finalize plugin method.
            Logging warning messages.
        """
        warnings.formatwarning = custom_formatwarning
        for i in range(len(result.todo)):
            warnings.warn('{}; error {} (in {})\n'.format(self.warnings_list[i][0], self.warnings_list[i][1], result.todo[i][0]))


def custom_formatwarning(msg, *a):
    # ignore everything except the message in warning
    return str(msg)


def warning(reason):
    """
    Decorator for skipping test by raising TodoWarningException with reason.
    """
    def decorator(test_item):
        @wraps(test_item)
        def wrapper(*args, **kwargs):
            try:
                test_item(*args, **kwargs)
            except KeyboardInterrupt:
                raise
            except AssertionError as e:
                raise TodoWarningException(reason, e)
            except Exception:
                raise
        return wrapper
    return decorator
