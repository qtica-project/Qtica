import re
import os
import platform
import socket
import sys
import webbrowser
from pathlib import Path
from .overload import staticproperty


class SystemType:
    @staticproperty
    def is_linux() -> bool:
        return platform.system() == "Linux"

    @staticproperty
    def is_linux_server() -> bool:
        if platform.system() == "Linux":
            # check if it's WSL
            p = "/proc/version"
            if os.path.exists(p):
                with open(p, "r") as file:
                    if "microsoft" in file.read():
                        return False  # it's WSL, not a server
            return os.environ.get("XDG_CURRENT_DESKTOP") is None
        return False

    @staticproperty
    def is_windows() -> bool:
        return platform.system() == "Windows"

    @staticproperty
    def is_macos() -> bool:
        return platform.system() == "Darwin"

    @staticproperty
    def is_java() -> bool:
        return platform.system() == "Java"


def get_platform():
    if (p := platform.system().lower()):
        return p

    raise Exception(f"Unsupported platform: {p}")


def get_arch():
    a = platform.machine().lower()
    if a == "x86_64" or a == "amd64":
        return "amd64"
    elif a == "arm64" or a == "aarch64":
        return "arm64"
    elif a.startswith("arm"):
        return "arm_7"
    else:
        raise Exception(f"Unsupported architecture: {a}")


def open_in_browser(url):
    webbrowser.open(url)


# https://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
def which(program, exclude_exe=None):
    import os

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    for path in os.environ["PATH"].split(os.pathsep):
        exe_file = os.path.join(path, program)
        if is_exe(exe_file) and (
            exclude_exe is None
            or (exclude_exe is not None and exclude_exe.lower() != exe_file.lower())
        ):
            return exe_file

    return None


def is_within_directory(directory, target):
    abs_directory = os.path.abspath(directory)
    abs_target = os.path.abspath(target)

    prefix = os.path.commonprefix([abs_directory, abs_target])

    return prefix == abs_directory


def safe_tar_extractall(tar, path=".", members=None, *, numeric_owner=False):
    for member in tar.getmembers():
        member_path = os.path.join(path, member.name)
        if not is_within_directory(path, member_path):
            raise Exception("Attempted Path Traversal in Tar File")

    tar.extractall(path, members, numeric_owner=numeric_owner)


def is_localhost_url(url):
    return (
        "://localhost/" in url
        or "://localhost:" in url
        or "://127.0.0.1/" in url
        or "://127.0.0.1:" in url
    )


def get_package_root_dir():
    return str(Path(__file__).parent)


def get_package_bin_dir():
    return os.path.join(get_package_root_dir(), "bin")


def get_package_web_dir():
    web_root_dir = os.environ.get("FLET_WEB_PATH")
    return web_root_dir if web_root_dir else os.path.join(get_package_root_dir(), "web")


def get_free_tcp_port():
    sock = socket.socket()
    sock.bind(("", 0))
    return sock.getsockname()[1]


def get_current_script_dir():
    pathname = os.path.dirname(sys.argv[0])
    return os.path.abspath(pathname)


def get_pi_version():
    """Detect the version of the Raspberry Pi by reading the revision field value from '/proc/cpuinfo'
    See: https://www.raspberrypi.org/documentation/hardware/raspberrypi/revision-codes/README.md
    Based on: https://github.com/adafruit/Adafruit_Python_GPIO/blob/master/Adafruit_GPIO/Platform.py
    """  # noqa
    # Check if file exist
    if not os.path.isfile('/proc/cpuinfo'):
        return None

    with open('/proc/cpuinfo', 'r') as f:
        cpuinfo = f.read()

    # Match a line like 'Revision   : a01041'
    revision = re.search(r'^Revision\s+:\s+(\w+)$', 
                         cpuinfo, 
                         flags=re.MULTILINE | re.IGNORECASE)
    if not revision:
        # Couldn't find the hardware revision, assume it is not a Pi
        return None

    # Determine the Pi version using the processor bits using the new-style
    # revision format
    revision = int(revision.group(1), base=16)
    if revision & 0x800000:
        return ((revision & 0xF000) >> 12) + 1

    # If it is not using the new style revision format,
    # then it must be a Raspberry Pi 1
    return 1


def is_32bit():
    return sys.maxsize <= 2**32


def is_64bit():
    return sys.maxsize > 2**32