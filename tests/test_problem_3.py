from problems.problem_3 import convert_to_mandarin


def test_convert_to__mandarin_returns_translation_one_digit():
    assert convert_to_mandarin('9') == 'jiu'
