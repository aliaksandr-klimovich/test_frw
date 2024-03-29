# Documentation

## Requirements

### Entities

#### TestCase

- Should contain all necessary information (variables, methods, etc.) to run the test.
- Shall contain `run` method to start the test case execution.
- (?) Should provide live log.
- Shall contain methods to assert and check entities.
    - Assert shall cause test fail immediately.
    - Check method shall:
        - store failed result,
        - continue test execution,
    - Both methods shall update `TestVerdict` accordingly each call.

#### TestResult

- Shall contain `TestVerdict`.
- Shall contain checks and assertions results.
- Should provide test output.

#### TestRunner

- Should run `TestCase` in an isolated environment.
- Shall create instance of the `TestCase`.
- Shall create instance of the `TestResult`.
- Should bind `TestCase` and `TestResult`, i.e. create communication channel between them.
- Should destroy `TestCase` after its run to release resources.

#### TestSuite

- Shall group `TestCase`.
- (?) Should provide possibility to sort, prioritize test cases.
- (?) Shall provide mechanism for getting test cases one by one (like pop from stack).

#### TestLoader

- Shall locate test cases, group them to `TestSuite` and pass to `TestRunner`.


### Constraints

- Should be possibility to extend base classes like `TestCase`.
- Should be possibility to parametrize `TestCase`.
- Should be possibility to run tests in parallel.
- If test case fails, test result should be collected anyway.


### Corner cases

- How the output of the test case should be handled?
    - Printed to the stdout / not printed
    - Stored / not stored


## Implementation

- Can inherit from `TestCase` and write tests. `run` method of the test case is used to start the test.
- `Checker` class is implemented as a mixin for `TestCase` class. It contains all need methods to
  check and assert entities. `AssertionFail` can be used to fail the test. For now it is up to `Checker`
  to report test results to `TestResult` instance.
- `TestRunner` is a static class. It can run a test case via its `run` method. It invokes next steps:
    - Creates `TestResult` instance.
    - Creates `TestCase` instance.
    - Runs `TestCase` on the place.
    - Destroys `TestCase` after run.
    - Collects `TestResult`s and returns them.
- User is responsible for stdout and stderr. User can configure any logger.
  Any "significant" action is considered an event and shall be stored in test results.

### todos

- Implement api for checker: on_check, on_passed, on_failed...
- Implement "between" comparison.
- (?) Modify traceback-s to show only line where comparison is fired.
- Implement text test writer.
- Improve exception info logging.
