from setuptools import setup

setup(name='moodlepy',
      version='0.1.1',
      description='Client for moodle webservice',
      author='Habib Rohman',
      author_email="habibrohman@protonmail.com",
      url='https://github.com/hexatester/moodlepy',
      license="MIT",
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3.7",
      ],
      packages=["moodlepy"],
      install_requires=['python'
                        'requests'
                        'dacite'],
      entry_points={'console_scripts': ['moodlepy=moodlepy.__main__:main']})
