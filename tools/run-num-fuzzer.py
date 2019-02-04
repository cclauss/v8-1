#!/usr/bin/env python
#
# Copyright 2018 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# for py2/py3 compatibility
from __future__ import absolute_import

import sys

from .testrunner import num_fuzzer


if __name__ == "__main__":
  sys.exit(num_fuzzer.NumFuzzer().execute())
