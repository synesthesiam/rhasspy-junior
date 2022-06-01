# Copyright 2022 Michael Hansen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import typing
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class SpeechToTextRequest:
    """Request for speech to text processing"""


@dataclass
class SpeechToTextResult:
    """Result of speech to text processing"""

    text: str
    """Best transcript of speech"""


class SpeechToText(ABC):
    """Base class for speech to text engines"""

    def __init__(self, config: typing.Dict[str, typing.Any]):
        pass

    @abstractmethod
    def begin_speech(self, request: SpeechToTextRequest):
        """Start speech to text phrase"""

    @abstractmethod
    def process_chunk(self, chunk: bytes):
        """Process audio chunk"""

    @abstractmethod
    def end_speech(self) -> typing.Optional[SpeechToTextResult]:
        """End speech to text phrase"""

    def start(self):
        """Initialize engine"""

    def stop(self):
        """Uninitialize engine"""
