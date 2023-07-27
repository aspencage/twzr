import setuptools

setuptools.setup(
    name='twzr',
    version='0.0.1',
    author='Aspen Cage',
    author_email='aspen@abpartners.co',
    description='Tweezer: small data tools',
    long_description="This is mostly a test project",
    long_description_content_type="text/markdown",
    url='https://github.com/ab-partners/chopper',
    license='MIT',
    packages=['twzr'],
    install_requires=[
        'numpy',
        'pandas'
        ]
)