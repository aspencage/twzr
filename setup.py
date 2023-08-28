import setuptools

setuptools.setup(
    name='twzr',
    version='0.1.4',
    author='Aspen Cage',
    author_email='aspenncage@gmail.com',
    description='Tweezer: teeny tiny tools for data processing',
    long_description="Microfunctions to help make pandas data transformation workflows faster. For example, Why type `df.filter(regex=re.compile('column',re.IGNORECASE))` when you can type `f(df,'column')`?",
    long_description_content_type="text/markdown",
    url='https://github.com/aspencage/twzr',
    license='MIT',
    packages=['twzr'],
    install_requires=[
        'numpy',
        'pandas'
        ]
)