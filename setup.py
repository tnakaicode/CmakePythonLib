from distutils.core import setup, Extension

if __name__ == '__main__':
    setup(name='foo',
          version='${PACKAGE_VERSION}',
          package_dir={'': '${CMAKE_CURRENT_SOURCE_DIR}'},
          packages=['module'])