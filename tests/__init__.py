# -*- coding: utf-8 -*-
#
#  PowerDNS web api python client and interface (python-powerdns)
#
#  Copyright (C) 2018 Denis Pompilio (jawa) <denis.pompilio@gmail.com>
#
#  This file is part of python-powerdns
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the MIT License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  MIT License for more details.
#
#  You should have received a copy of the MIT License along with this
#  program; if not, see <https://opensource.org/licenses/MIT>.

import powerdns

from logging import Logger
from unittest import TestCase


PDNS_KEY = "MySupErS3cureK3y"
PDNS_API = "http://localhost:8081/api/v1"

API_CLIENT = powerdns.PDNSApiClient(
    api_endpoint=PDNS_API, api_key=PDNS_KEY, verify=False
)


class TestLogger(TestCase):
    def test_logger_creation(self):
        self.assertIsInstance(powerdns.basic_logger("test", 2, 1), Logger)
