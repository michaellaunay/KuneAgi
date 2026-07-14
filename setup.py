import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

requires = [
    'babel',
    'dogpile.cache',
    'ecreall_dace',
    'ecreall_pontus',
    'ecreall_daceui',
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_layout',
    'pyramid_mailer',
    'pyramid_retry',
    'pyramid_tm',
    'requests',
    'deform',
    'substanced',
    'mock', # test dependency of substanced, needed because of venusian scan
    'waitress',
    'gunicorn',
    'plone.event',
    'xlrd',
    'html_diff_wrapper',
    'Genshi',
    'beautifulsoup4',
    'profilehooks',
    'metadata_parser',
    'deform_treepy',
    'numpy',
    'randomcolor',
    'graphene',
    'graphql-wsgi',
    'keas.kmi',
    'cipher.encryptingstorage',
    'yampy2',
    'ovh',
    'pyramid-sms',
    'velruse'
    ]

setup(name='novaideo',
      version='1.4.dev0',
      description='Nova-Ideo is a participatory innovation tool, the merger of the box ideas and collaborative portal.',
      long_description=README + '\n\n' +  CHANGES,
      long_description_content_type='text/markdown',
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        ],
      author='Amen Souissi',
      author_email='amensouissi@ecreall.com',
      maintainer='Michaël Launay (Logikascium)',
      url='https://github.com/michaellaunay/KuneAgi/',
      project_urls={
          'Source': 'https://github.com/michaellaunay/KuneAgi',
          'Tracker': 'https://github.com/michaellaunay/KuneAgi/issues',
          'Historical upstream (KuneAgi)': 'https://github.com/ecreall/KuneAgi',
          'Historical upstream (nova-ideo)': 'https://github.com/ecreall/nova-ideo',
      },
      keywords='web pyramid substanced',
      license="AGPLv3+",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="novaideo",
      message_extractors={
          'novaideo': [
              ('**.py', 'python', None), # babel extractor supports plurals
              ('**.pt', 'chameleon', None),
          ],
      },
      extras_require = dict(
          test=['pyramid_robot'],
      ),
      entry_points="""\
      [paste.app_factory]
      main = novaideo:main
      """,
      )

