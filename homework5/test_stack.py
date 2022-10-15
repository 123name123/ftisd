import pytest
from stack_oop import Stack
from stack_func import init, pop, push, empty, top, size


@pytest.fixture(scope="module")
def oop_stack_generator():
    yield Stack()


def test_oop_stack_empty_true(oop_stack_generator):
    assert oop_stack_generator.empty()


def test_oop_stack_push(oop_stack_generator):
    oop_stack_generator.push(1)
    oop_stack_generator.push(2)
    oop_stack_generator.push(3)
    assert oop_stack_generator.size() == 3


def test_oop_stack_top_push(oop_stack_generator):
    assert oop_stack_generator.top() == 3


def test_oop_stack_pop(oop_stack_generator):
    assert oop_stack_generator.pop() == 3
    assert oop_stack_generator.size() == 2
    assert oop_stack_generator.top() == 2


def test_oop_stack_empty_false(oop_stack_generator):
    assert not oop_stack_generator.empty()


def test_oop_stack_size(oop_stack_generator):
    assert oop_stack_generator.size() == 2


def test_oop_stack_pop_from_empty_stack(oop_stack_generator):
    assert oop_stack_generator.pop() == 2
    assert oop_stack_generator.pop() == 1
    assert oop_stack_generator.empty()
    assert oop_stack_generator.size() == 0
    assert oop_stack_generator.pop() is None
    assert oop_stack_generator.pop() is None


@pytest.fixture
def func_stack_generator():
    yield init()


def test_func_empty_true(func_stack_generator):
    assert empty(func_stack_generator)


def test_func_push(func_stack_generator):
    assert size(push(push(push(func_stack_generator, 1), 2), 3)) == 3


def test_func_empty_false(func_stack_generator):
    assert not empty(push(func_stack_generator, 1))


def test_func_top(func_stack_generator):
    assert top(push(push(push(func_stack_generator, 1), 2), 3)) == 3
    assert top(push(push(func_stack_generator, 1), 2)) == 2
    assert top(push(func_stack_generator, 1)) == 1


def test_func_pop(func_stack_generator):
    assert pop(push(push(push(func_stack_generator, 1), 2), 3)) == [1, 2]
    assert pop(pop(push(push(push(func_stack_generator, 1), 2), 3))) == [1]
    assert pop(pop(pop(push(push(push(func_stack_generator, 1), 2), 3)))) == []


def test_func_pop_from_empty_stack(func_stack_generator):
    assert empty(func_stack_generator)
    assert pop(func_stack_generator) is func_stack_generator
    assert pop(func_stack_generator) is func_stack_generator
    assert pop(func_stack_generator) is func_stack_generator


def test_func_top_from_empty_stack(func_stack_generator):
    assert empty(func_stack_generator)
    assert top(func_stack_generator) is None
