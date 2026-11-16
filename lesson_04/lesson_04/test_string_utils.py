import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# ==========================================
# Тесты для функции capitalize
# ==========================================
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("Тест", "Тест"),  # не пустая строка
        ("123", "123"),  # числа как строка
        ("04 апреля 2023", "04 апреля 2023"),  # строка с пробелами
    ],
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str",
    [
        "",  # Пустая строка
        " ",  # Строка с пробелом
        None,  # None
        [],  # Пустой список
    ],
)
def test_capitalize_negative(input_str):
    with pytest.raises((AttributeError, TypeError)):
        string_utils.capitalize(input_str)


# ==========================================
# Тесты для функции trim
# ==========================================
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   Тест", "Тест"),
        ("  123", "123"),
        ("  04 апреля 2023", "04 апреля 2023"),
    ],
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),  # Пустая строка
        ("   ", ""),  # Строка с пробелом (все удалятся)
    ],
)
def test_trim_negative_empty_or_spaces(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str",
    [
        None,  # None
        [],  # Пустой список
    ],
)
def test_trim_negative_invalid_types(input_str):
    with pytest.raises((AttributeError, TypeError)):
        string_utils.trim(input_str)


# ==========================================
# Тесты для функции contains
# ==========================================
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("Тест", "е", True),
        ("123", "2", True),
        ("04 апреля 2023", " ", True),  # пробел содержится
    ],
)
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("Тест", "ю", False),
        ("", "a", False),  # Пустая строка
        (" ", "a", False),  # Строка с пробелом
    ],
)
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol",
    [
        (None, "a"),  # None как строка
        ("Тест", None),  # None как символ
        ([], "a"),  # Пустой список
    ],
)
def test_contains_negative_invalid_types(input_str, symbol):
    with pytest.raises((AttributeError, TypeError)):
        string_utils.contains(input_str, symbol)


# ==========================================
# Тесты для функции delete_symbol
# ==========================================
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("Тест", "е", "Тст"),
        ("1232", "2", "13"),
        ("04 апреля 2023", " ", "04апреля2023"),
    ],
)
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("Тест", "ю", "Тест"),  # Символа нет
        ("", "a", ""),  # Пустая строка
        ("   ", " ", ""),  # Строка с пробелом
    ],
)
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol",
    [
        (None, "a"),  # None как строка
        ("Тест", None),  # None как символ
        ([], "a"),  # Пустой список
    ],
)
def test_delete_symbol_negative_invalid_types(input_str, symbol):
    with pytest.raises((AttributeError, TypeError)):
        string_utils.delete_symbol(input_str, symbol)
