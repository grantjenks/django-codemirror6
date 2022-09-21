import django_codemirror6 as codemirror6


def test_version():
    assert tuple(map(int, codemirror6.__version__.split('.'))) > (0, 0, 0)


def test_title():
    assert codemirror6.__title__ == 'django-codemirror6'
