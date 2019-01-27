#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostStatechartConan(base.BoostBaseConan):
    name = "boost_statechart"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_statechart"
    lib_short_names = ["statechart"]
    header_only_libs = ["statechart"]
    b2_requires = [
        "boost_assert",
        "boost_bind",
        "boost_config",
        "boost_conversion",
        "boost_core",
        "boost_detail",
        "boost_function",
        "boost_mpl",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_thread",
        "boost_type_traits"
    ]
