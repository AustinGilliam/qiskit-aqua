# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

from .variational_form import VariationalForm
from .ry import RY
from .ryrz import RYRZ
from .swaprz import SwapRZ
# try:
#     from .uccsd import UCCSD
# except ImportError:
#     raise ImportWarning('UCCSD can be only used with qiskit_aqua_chemistry lib." \
#         "If you would like to use it for other purposes," \
#         "please install qiskit_aqua_chemistry first."')

__all__ = ['VariationalForm',
           'RY',
           'RYRZ',
           'SwapRZ']
