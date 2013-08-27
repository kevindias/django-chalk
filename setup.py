from setuptools import setup


setup(name='django-chalk',
      version='0.2.1',
      author='Kevin Dias',
      author_email='kevin@kevindias.com',
      description='Simple reStructuredText blogging for Django',
      url='http://kevindias.com/projects/chalk/',
      packages=['chalk'],
      install_requires=['docutils>=0.9', 'pygments>=1.4'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Framework :: Django',
                   'Topic :: Utilities'],
      zip_safe=False,
)
