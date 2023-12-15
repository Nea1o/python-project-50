from gendiff.generate import generate_diff


def test_gendiff_func():
    result = generate_diff(
        "/home/neal/Рабочий стол/Study/Project2/gendiff/tests/fixtures/file1.json",
        "/home/neal/Рабочий стол/Study/Project2/gendiff/tests/fixtures/file2.json")
    assert result == "{ \n  - follow: false \n    host: hexlet.io \n  - proxy: 123.234.53.22 \n  - timeout: 50 \n  + timeout: 20 \n  + verbose: true \n}"
