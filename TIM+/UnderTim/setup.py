from distutils.core import setup, Extension
from Cython.Distutils import build_ext
from distutils.extension import Extension

sources_list = ["undertim.pyx", "Graph.cpp", "InfGraph.cpp", "TimGraph.cpp", "sfmt/SFMT.c"]

setup(ext_modules=[Extension("undertim", sources=sources_list,language="c++",extra_compile_args=["-std=c++11"])],cmdclass={'build_ext':build_ext})