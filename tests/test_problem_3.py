from problems.problem_3 import convert_to_mandarin


'''
Preliminary test cases
convert_to_mandarin('36') will return san shi liu
convert_to_mandarin('20') will return er shi
convert_to_mandarin('16') will return shi liu
'''


def test_convert_to__mandarin_returns_translation_one_digit():
    assert convert_to_mandarin('9') == 'jiu'


def test_convert_to__mandarin_returns_translation_two_digits_11():
    assert convert_to_mandarin('11') == 'shi yi'


def test_convert_to__mandarin_returns_translation_two_digits_16():
    assert convert_to_mandarin('16') == 'shi liu'
