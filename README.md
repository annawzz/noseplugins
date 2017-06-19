# noseplugins

### TodoWarningPlugin is used for passing 'broken' tests.

When test, decorated with this plugin, fails, 'W' or 'Warning' will be in output.
If this test passes, a dot '.' will be in output.

Example of using:

```python
from nose_todo_plugin import warning
...

    @warning("reason of fail")
    def test_empty_listing(self):
    ...
```

Also, in setup.cfg add option 'with-todo=1'.

In the final test results, all warnings will be outputed in format:
```
Reason of fail: Exception from test falling (name of test case).
```
