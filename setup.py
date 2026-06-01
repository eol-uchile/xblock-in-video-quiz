"""Setup for invideoquiz XBlock."""

import setuptools

setuptools.setup(
    name='invideoquiz-xblock',
    version='1.0.0',
    description='Helper XBlock to locate CAPA problems within videos.',
    license='AGPL v3',
    author="Oficina EOL UChile",
    author_email="eol-ing@uchile.cl",
    url="https://eol.uchile.cl",
    packages=setuptools.find_packages(),
    install_requires=[
        'django >= 1.8',
        'django_nose',
        'mock',
        'coverage',
        'mako',
        'XBlock',
        'xblock-utils',
    ],
    dependency_links=[
        'https://github.com/openedx-unsupported/xblock-utils/tarball/c39bf653e4f27fb3798662ef64cde99f57603f79#egg=xblock-utils',
    ],
    entry_points={
        'xblock.v1': [
            'invideoquiz = invideoquiz.invideoquiz:InVideoQuizXBlock',
        ],
         'lms.djangoapp': [
            "invideoquiz = invideoquiz.apps:InVideoQuizConfig",
        ],
        'cms.djangoapp': [
            "invideoquiz = invideoquiz.apps:InVideoQuizConfig",
        ]
    }
)
