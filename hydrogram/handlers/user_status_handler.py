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

from typing import Callable

from .handler import Handler


class UserStatusHandler(Handler):
    """The UserStatus handler class. Used to handle user status updates (user going online or offline).
    It is intended to be used with :meth:`~hydrogram.Client.add_handler`.

    For a nicer way to register this handler, have a look at the :meth:`~hydrogram.Client.on_user_status` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new user status update arrives. It takes *(client, user)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of users to be passed in your callback function.

    Other parameters:
        client (:obj:`~hydrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the user status handler.

        user (:obj:`~hydrogram.types.User`):
            The user containing the updated status.
    """

    def __init__(self, callback: Callable, filters=None):
        super().__init__(callback, filters)
