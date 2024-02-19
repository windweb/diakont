from enum import Enum
from typing import Tuple


class RequestTypes(str, Enum):
    SCOPE = "Scope"


class ScopeModes(str, Enum):
    FORCE = "Force"
    ONCE = "Once"
    CYCLIC = "Cyclic"
    REPEAT = "Repeat"


class ScopeConditions(str, Enum):
    EQUAL = "Equal"
    NON_EQUAL = "NonEqual"
    LESS = "Less"
    GREAT = "Great"


class ScopeMethods(str, Enum):
    REQUEST = "request"
    DOWNLOAD = "download"
    SETUP = "setup"
    RESET = "reset"
