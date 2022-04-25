#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2023-present Amano LLC <https://amanoteam.com>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from hydrogram.types.object import Object


class ForumTopicReopened(Object):
    """A service message about a forum topic reopened in the chat.

    Currently holds no information.
    """

    def __init__(self):
        super().__init__()