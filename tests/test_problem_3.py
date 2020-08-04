from problems.problem_3 import convert_to_mandarin


'''
Preliminary test cases
convert_to_mandarin('36') will return san shi liu
convert_to_mandarin('20') will return er shi
convert_to_mandarin('16') will return shi liu
'''


def test_convert_to__mandarin_returns_translation_one_digit():
    assert convert_to_mandarin('9') == 'jiu'


def test_convert_to__mandarin_returns_1_for_teens():
    assert convert_to_mandarin('11') == 'shi yi'


def test_convert_to__mandarin_returns_translation_two_digits_16():
    assert convert_to_mandarin('16') == 'shi liu'


def test_convert_to__mandarin_returns_translation_two_digits_20():
    assert convert_to_mandarin('20') == 'er shi'


def test_convert_to__mandarin_returns_other_for_31():
    assert convert_to_mandarin('31') == 'san shi yi'


def test_convert_to__mandarin_returns_other_for_36():
    assert convert_to_mandarin('36') == 'san shi liu'
