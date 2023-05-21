from setuptools import setup

setup(name='postgres_connector',
      version='0.2',
      description='A Postgresql Database Connector',
      url='#',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['postgres_connector'],
      zip_safe=False,
      install_requires=[
        'psycopg2',
        ],
      )
