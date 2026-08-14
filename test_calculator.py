import pytest
from a import Calculator, ScientificCalculator


class TestCalculator:
    """Test suite for Calculator class"""

    def setup_method(self):
        """Initialize calculator before each test"""
        self.calc = Calculator()

    def test_add(self):
        """Test addition operation"""
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(-5, 3) == -2
        assert self.calc.add(0, 0) == 0

    def test_subtract(self):
        """Test subtraction operation"""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(-5, 3) == -8
        assert self.calc.subtract(0, 0) == 0

    def test_multiply(self):
        """Test multiplication operation"""
        assert self.calc.multiply(5, 3) == 15
        assert self.calc.multiply(-5, 3) == -15
        assert self.calc.multiply(0, 5) == 0

    def test_divide(self):
        """Test division operation"""
        assert self.calc.divide(6, 3) == 2
        assert self.calc.divide(-6, 3) == -2
        assert self.calc.divide(5, 2) == 2.5

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)


class TestScientificCalculator:
    """Test suite for ScientificCalculator class"""

    def setup_method(self):
        """Initialize scientific calculator before each test"""
        self.sci_calc = ScientificCalculator()

    def test_power(self):
        """Test power operation"""
        assert self.sci_calc.power(2, 3) == 8
        assert self.sci_calc.power(5, 0) == 1
        assert self.sci_calc.power(-2, 2) == 4

    def test_square_root(self):
        """Test square root operation"""
        assert self.sci_calc.square_root(16) == 4
        assert self.sci_calc.square_root(0) == 0
        assert abs(self.sci_calc.square_root(2) - 1.414) < 0.001

    def test_square_root_negative(self):
        """Test square root of negative number raises ValueError"""
        with pytest.raises(ValueError, match="Cannot take the square root of a negative number"):
            self.sci_calc.square_root(-4)

    def test_inherited_methods(self):
        """Test that ScientificCalculator inherits Calculator methods"""
        assert self.sci_calc.add(5, 3) == 8
        assert self.sci_calc.multiply(2, 4) == 8
