# errortext

`errortext` is a Python package to provide error messages for Python
exceptions, even if the original message is empty.

As example consider the following function that might fail in different ways:

```python
from errortext import error_text

def do_something(action_to_perform):
    if action_to_perform == "walk":
        print("walking")
    elif action_to_perform == "sleep":
        raise ValueError("must be tired in order to sleep")
    elif action_to_perform == "run":
        raise NotImplementedError("run")
    else:
        assert False
```

One could use the following code to run this function and print possible
error details by using the error message of the exception from
`str(error)`:

```python
try:
    do_something(action)
    print(f"Success: done with {action}")
except Exception as error:
    print(f"Error: cannot {action}: {str(error)}")
```

As you notice, some error will not have any meaningful message:

```
do_something("sleep") -> cannot sleep: must be tired in order to sleep
do_something("run")   -> cannot run: run
do_something("xxx")   -> cannot xxx:
```

No change the error handler to:

```python
print(f"Error with error_text: cannot {action}: {error_text(error)}")
```

The error messages will at least contain some hint at what went wrong:

```
do_something("sleep") -> cannot sleep: must be tired in order to sleep
do_something("run")   -> cannot run: NotImplementedError: run
do_something("xxx")   -> cannot xxx: AssertionError
```
