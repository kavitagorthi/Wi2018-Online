import pytest
import random
from simple_circle_class import Circle
from simple_circle_class import Sphere


########
# Step 1
########
def test_init():
    c = Circle(4)
    assert c.radius == 4


########
# Step 2
########
def test_diam_prop():
    c = Circle(4)
    assert c.diameter == 8


########
# Step 3
########
def test_diam_setter():
    c = Circle(4)
    c.diameter = 2
    assert c.radius == 1
    assert c.diameter == 2


########
# Step 4
########
def test_area():
    c = Circle(2)
    assert c.area == pytest.approx(12.566370)

def test_area_attr_error():
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area = 42


########
# Step 5
########
def test_alt_constr_diam():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


########
# Step 6
########
def test_str(capsys):
    c = Circle(4)
    print(c)
    out, _ = capsys.readouterr()
    assert out.strip() == "Circle with radius: 4.000000"

def test_repr():
    c = Circle(4)
    assert repr(c) == "Circle(4)"
    d = eval(repr(c))
    assert d == Circle(4)  # Circle.__eq__ must be implemented to compare!

def test_eq():
    c1 = Circle(4)
    c2 = Circle(4)
    assert c1 == c2

########
# Step 7
########
def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == Circle(6)

def test_mul():
    assert Circle(4) * 3 == Circle(12)

def test_rmul():
    assert 3 * Circle(4) == Circle(12)


########
# Step 8
########
# The code was written before these tests, at Step 6, when testing __repr__
def test_comparison():
    """Test if @functools.total_ordering really works."""
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 > c2) is False
    assert (c1 < c2) is True
    assert (c1 == c2) is False
    c3 = Circle(4)
    assert (c2 == c3) is True

def test_sort():
    circles = []
    for i in range(0, 11):
        circles.append(Circle(i))
    random.shuffle(circles)
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3),
                       Circle(4), Circle(5), Circle(6), Circle(7),
                       Circle(8), Circle(9), Circle(10)]


########
# Step 8 - Optional Features
########
def test_reflected_numerics():
    a_circle = Circle(2)
    assert (a_circle * 3) == (3 * a_circle)


def test_negative_radius():
    with pytest.raises(ValueError):
        c = Circle(-1)

def test_sub_circle():
    a_circle = Circle(4)
    c3 = a_circle - Circle(1)
    assert c3 == Circle(3)


def test_augmented_assignments():
    a_circle = Circle(2)
    a_circle += Circle(3)
    assert a_circle == Circle(5)
    a_circle = Circle(2)
    a_circle *= 4
    assert a_circle == Circle(8)
    a_circle = Circle(3)
    a_circle -= Circle(2)
    assert a_circle == Circle(1)


########
# Step 9 - Subclassing
########
def test_init_sphere():
    s = Sphere(3)
    assert round(s.volume, 3) == pytest.approx(113.097)

def test_str_sphere(capsys):
        s = Sphere(4)
        print(s)
        out, _ = capsys.readouterr()
        assert out.strip() == "Sphere with radius: 4.000000"

def test_repr_shere():
    s = Sphere(4)
    assert repr(s) == "Sphere(4)"
    d = eval(repr(s))
    assert d == Sphere(4)

def test_alt_constr_diam_sphere():
    s = Sphere.from_diameter(8)
    assert s.diameter == 8
    assert s.radius == 4
