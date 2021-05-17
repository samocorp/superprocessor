# Tests

### Testing in Development

Run tests locally by invoking the shell script

    ./run.sh
    
which iterates over all files named `test*.py` in the directory
and invokes them all with a python3 interpreter.

### Creating new Tests

Creating tests is easy. Simply create a new file named `test_<TESTNAME>.py`
that asserts values to be as expected when invoked directly
