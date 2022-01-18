import sys
from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="mylib-rust",
    version="1.0",
    # build a rust2py library in the rust2py/ folder
    rust_extensions=[RustExtension("rust2py.rust2py", binding=Binding.RustCPython)],
    packages=["rust2py"],
    # Rust extensions are not zip safe
    zip_safe=False,
    long_description="This is a description for our Rust-Python package.",
    long_description_content_type="text/x-rst"
)
