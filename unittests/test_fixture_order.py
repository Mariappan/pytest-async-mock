import pytest

# fixtures documentation order example
order = []


@pytest.fixture(scope="session")
def session():
    order.append("session")


@pytest.fixture(scope="module")
def module():
    order.append("module")


@pytest.fixture
def func1(func3):
    order.append("func1")


@pytest.fixture
def func3():
    order.append("func3")


@pytest.fixture(autouse=True)
def autouse():
    order.append("autouse")


@pytest.fixture
def func2():
    order.append("func2")


def test_order(func1, module, func2, session):
    print(f"The order of inclusion is:\n {order}")

    """
    The fixtures requested by test_order will be instantiated in the following order:

    s1: is the highest-scoped fixture (session).
    m1: is the second highest-scoped fixture (module).
    a1: is a function-scoped autouse fixture: it will be instantiated before other fixtures within the same scope.
    f3: is a function-scoped fixture, required by f1: it needs to be instantiated at this point
    f1: is the first function-scoped fixture in test_order parameter list.
    f2: is the last function-scoped fixture in test_order parameter list.
    """
    assert order == ["session", "module", "autouse", "func3", "func1", "func2"]
