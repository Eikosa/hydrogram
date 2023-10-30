#  Hydrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2023 Dan <https://github.com/delivrance>
#  Copyright (C) 2023-present Amano LLC <https://amanoteam.com>
#
#  This file is part of Hydrogram.
#
#  Hydrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Hydrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Hydrogram.  If not, see <http://www.gnu.org/licenses/>.

from enum import auto

from .auto_name import AutoName


class UserStatus(AutoName):
    """User status enumeration used in :obj:`~hydrogram.types.User`."""

    ONLINE = auto()
    """User is online"""

    OFFLINE = auto()
    """User is offline"""

    RECENTLY = auto()
    """User was seen recently"""

    LAST_WEEK = auto()
    """User was seen last week"""

    LAST_MONTH = auto()
    """User was seen last month"""

    LONG_AGO = auto()
    """User was seen long ago"""
