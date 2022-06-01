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

import argparse
from pathlib import Path


_DIR = Path(__file__).parent


def get_args() -> argparse.Namespace:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--config",
        required=True,
        action="append",
        help="Path to TOML configuration file",
    )

    parser.add_argument(
        "--debug", action="store_true", help="Print DEBUG messages to the console"
    )

    args = parser.parse_args()

    # Convert to paths
    args.config = [Path(p) for p in args.config]

    return args