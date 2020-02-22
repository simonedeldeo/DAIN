#!/usr/bin/env python3
import os
import torch

from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

cxx_args = ['-std=c++11']

nvcc_args = [
    '-gencode', 'arch=compute_75,code=sm_75',
    '-gencode', 'arch=compute_52,code=sm_52',
    '-gencode', 'arch=compute_60,code=sm_60',
    '-gencode', 'arch=compute_61,code=sm_61'
    # '-gencode', 'arch=compute_70,code=sm_70',
    # '-gencode', 'arch=compute_70,code=compute_70'
]

setup(
    name='interpolationch_cuda',
    ext_modules=[
        CUDAExtension('interpolationch_cuda', [
            'interpolationch_cuda.cc',
            'interpolationch_cuda_kernel.cu'
        ], extra_compile_args={'cxx': cxx_args, 'nvcc': nvcc_args})
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
