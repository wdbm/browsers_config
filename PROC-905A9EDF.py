#!/usr/bin/env python3

"""
################################################################################
#                                                                              #
# PROC-905A9EDF                                                                #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This programme creates a self-contained local Firefox installation and       #
# profile.                                                                     #
#                                                                              #
# copyright (C) 2026 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses>.                                               #
#                                                                              #
################################################################################

Usage:
    PROC-905A9EDF.py [--directory=<path>] [--profile=<name>] [--firefox-version=<version>]
    PROC-905A9EDF.py (-h | --help)
    PROC-905A9EDF.py --version

Options:
    -d <path>, --directory=<path>              Installation directory. By default,
                                                 Firefox_<profile> is created at the
                                                 working directory.
    -p <name>, --profile=<name>                Profile name. A UUID4T8 is generated
                                                 by default.
    -f <version>, --firefox-version=<version>  Firefox version [default: 155.0.1].
    -h, --help                                 Show this help text.
    --version                                  Show the script version.
"""

from __future__ import annotations

import inspect
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tarfile
import unicodedata
import urllib.error
import urllib.request
import uuid

try:
    from docopt import docopt
except ModuleNotFoundError as error:
    if error.name != "docopt":
        raise
    print("Error: docopt is required; install it with 'python3 -m pip install docopt'.", file=sys.stderr)
    sys.exit(1)


__VERSION__ = "2026-09-14T1827Z"
FIREFOX_DOWNLOAD_ROOT = "https://download-installer.cdn.mozilla.net/pub/firefox/releases"
VERSION_PATTERN = re.compile(r"[0-9]+(?:\.[0-9]+){1,3}(?:[A-Za-z][A-Za-z0-9.-]*)?")
UNSAFE_FILENAME_CHARACTERS = re.compile(r"[^A-Za-z0-9._-]+")


def generate_uuid4t8() -> str:
    """Generate the first eight UUID4 characters, including at least one letter."""
    while True:
        identifier = str(uuid.uuid4())[:8]
        if any(character.isalpha() for character in identifier):
            return identifier


def make_filename_safe(value: str) -> str:
    """Return a conservative, filename-safe form of a profile name."""
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    safe_value = UNSAFE_FILENAME_CHARACTERS.sub("_", ascii_value.strip()).strip("._-")
    if not safe_value or safe_value in {".", ".."}:
        raise ValueError("the profile name does not contain any filename-safe characters")
    return safe_value


def validate_version(version: str) -> str:
    """Validate a Firefox release version before it is used in paths and a URL."""
    if not VERSION_PATTERN.fullmatch(version):
        raise ValueError(f"invalid Firefox version: {version!r}")
    return version


def ensure_empty_directory(directory: Path) -> bool:
    """Create an installation directory, or verify that it is an empty directory."""
    if directory.exists():
        if not directory.is_dir():
            raise ValueError(f"the installation path is not a directory: {directory}")
        if any(directory.iterdir()):
            raise ValueError(f"the installation directory is not empty: {directory}")
        return False

    directory.mkdir(parents=True)
    return True


def download_file(url: str, destination: Path) -> None:
    """Download a URL to a local file."""
    request = urllib.request.Request(url, headers={"User-Agent": "PROC-905A9EDF/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        with destination.open("wb") as output_file:
            shutil.copyfileobj(response, output_file)


def download_firefox_archive(version: str, destination: Path) -> Path:
    """Download the available Linux archive format for a Firefox release."""
    archive_names = (
        f"firefox-{version}.tar.xz",
        f"firefox-{version}.tar.bz2",
    )
    for archive_name in archive_names:
        archive_path = destination / archive_name
        url = f"{FIREFOX_DOWNLOAD_ROOT}/{version}/linux-x86_64/en-US/{archive_name}"
        print(f"Downloading Firefox {version} from {url}")
        try:
            download_file(url, archive_path)
        except urllib.error.HTTPError as error:
            archive_path.unlink(missing_ok=True)
            if error.code != 404:
                raise
        else:
            return archive_path

    raise ValueError(f"no Linux x86-64 archive was found for Firefox {version}")


def validate_archive_members(members: list[tarfile.TarInfo]) -> None:
    """Reject archive entries which could write outside the extraction directory."""
    for member in members:
        member_path = PurePosixPath(member.name)
        if member_path.is_absolute() or ".." in member_path.parts:
            raise ValueError(f"unsafe path at Firefox archive: {member.name!r}")
        if member.ischr() or member.isblk() or member.isfifo():
            raise ValueError(f"unsupported special file at Firefox archive: {member.name!r}")
        if member.issym() or member.islnk():
            link_path = PurePosixPath(member.linkname)
            if link_path.is_absolute():
                raise ValueError(f"unsafe link at Firefox archive: {member.name!r}")
            if member.issym():
                link_path = member_path.parent / link_path
            normalised_parts: list[str] = []
            for part in link_path.parts:
                if part in {"", "."}:
                    continue
                if part == "..":
                    if not normalised_parts:
                        raise ValueError(f"unsafe link at Firefox archive: {member.name!r}")
                    normalised_parts.pop()
                else:
                    normalised_parts.append(part)


def extract_archive(archive_path: Path, destination: Path) -> None:
    """Extract a Firefox archive after checking every member path."""
    with tarfile.open(archive_path, mode="r:*") as archive:
        members = archive.getmembers()
        validate_archive_members(members)
        if "filter" in inspect.signature(archive.extractall).parameters:
            archive.extractall(destination, members=members, filter="data")
        else:
            archive.extractall(destination, members=members)


def write_launcher(path: Path, installation_name: str, profile_name: str) -> None:
    """Write the Bash launcher which resolves all paths relative to itself."""
    launcher = f'''#!/usr/bin/env bash
set -euo pipefail

script_directory="$(cd -- "$(dirname -- "${{BASH_SOURCE[0]}}")" && pwd)"
exec "${{script_directory}}/{installation_name}/firefox" --allow-downgrade -profile "${{script_directory}}/{profile_name}" "${{@}}"
'''
    path.write_text(launcher, encoding="utf-8")
    path.chmod(0o755)


def install_firefox(directory: Path, profile_name: str, version: str) -> None:
    """Download and prepare Firefox, its profile directory, and its launcher."""
    installation_name = f"firefox-{version}"
    reserved_names = {
        f"firefox-{version}.tar.xz",
        f"firefox-{version}.tar.bz2",
        installation_name,
        "run.sh",
    }
    if profile_name in reserved_names:
        raise ValueError(f"the profile name is reserved for the installation: {profile_name!r}")

    directory_created = ensure_empty_directory(directory)
    staging_directory = directory / f".installing-{generate_uuid4t8()}"
    staging_directory.mkdir()
    extraction_directory = staging_directory / "extracted"
    extraction_directory.mkdir()

    committed_paths: list[Path] = []
    try:
        archive_path = download_firefox_archive(version, staging_directory)

        print(f"Extracting {archive_path.name}")
        extract_archive(archive_path, extraction_directory)
        extracted_firefox = extraction_directory / "firefox"
        if not (extracted_firefox / "firefox").is_file():
            raise ValueError("the Firefox archive does not have the expected structure")
        extracted_firefox.rename(staging_directory / installation_name)
        extraction_directory.rmdir()

        (staging_directory / profile_name).mkdir()
        write_launcher(staging_directory / "run.sh", installation_name, profile_name)

        for item_name in (archive_path.name, installation_name, profile_name, "run.sh"):
            committed_path = directory / item_name
            (staging_directory / item_name).rename(committed_path)
            committed_paths.append(committed_path)
        staging_directory.rmdir()
    except BaseException:
        shutil.rmtree(staging_directory, ignore_errors=True)
        for committed_path in reversed(committed_paths):
            if committed_path.is_dir() and not committed_path.is_symlink():
                shutil.rmtree(committed_path, ignore_errors=True)
            else:
                committed_path.unlink(missing_ok=True)
        if directory_created:
            try:
                directory.rmdir()
            except OSError:
                pass
        raise

    print(f"Firefox was installed at: {directory / installation_name}")
    print(f"The profile was created at: {directory / profile_name}")
    print(f"Firefox can be launched with: {directory / 'run.sh'}")


def main() -> int:
    """Parse command line options and run the installation."""
    options = docopt(__doc__, version=__VERSION__)
    try:
        supplied_profile = options["--profile"]
        profile_name = make_filename_safe(supplied_profile) if supplied_profile else generate_uuid4t8()
        version = validate_version(options["--firefox-version"])
        supplied_directory = options["--directory"]
        directory = (
            Path(supplied_directory).expanduser().resolve()
            if supplied_directory
            else (Path.cwd() / f"Firefox_{profile_name}").resolve()
        )

        if supplied_profile and profile_name != supplied_profile:
            print(f"The profile name was made filename-safe: {profile_name}")
        install_firefox(directory, profile_name, version)
    except (OSError, ValueError, tarfile.TarError, urllib.error.URLError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nInstallation interrupted.", file=sys.stderr)
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())
