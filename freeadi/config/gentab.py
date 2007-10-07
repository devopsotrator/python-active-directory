#!/usr/bin/env python
#
# This file is part of FreeADI. FreeADI is free software and is made available
# under the terms of the GNU General Public License, version 3. Consult the
# file "LICENSE" that is distributed together with this file for the exact
# licensing terms.
#
# FreeADI is copyright (c) 2007 by the FreeADI authors. See the file "AUTHORS"
# for a complete overview.

# This script generates the PLY parser tables. Note: It needs to be run from
# the directory holding the parsers!!

from freeadi.config.parse_krb5 import Krb5Parser
from freeadi.config.parse_ldap import LdapParser

parser = Krb5Parser()
parser._write_parsetab()

parser = LdapParser()
parser._write_parsetab()