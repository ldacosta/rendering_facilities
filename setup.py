from distutils.core import setup

setup(
    name='RenderingFacilities',
    version='0.1.0',
    author='Luis Da Costa',
    author_email='dacosta.le@gmail.com',
    packages=['rendering', 'rendering.pygame'],
    scripts=[],
    url='https://github.com/ldacosta/rendering_facilities/',
    license='LICENSE.txt',
    description='Useful rendering facilities.',
    long_description=open('README.txt').read(),
    install_requires=[
        "astroid >= 1.5.3",
        "Geometry2D >= 0.7.0",
        "pygame >= 1.9.3",
        "pylint"
    ],
)
