import os

from tide_agent.win import browser, capture, devices, input, net, procs, windows


def _open_path(path: str) -> None:
    """Open a file or folder the way double-clicking it would (PDF viewer, Explorer…)."""
    try:
        os.startfile(path)
    except OSError:
        pass


class WinPlatform:
    foreground = staticmethod(windows.foreground)
    browser_host = staticmethod(browser.browser_host)
    processes = staticmethod(procs.processes)
    kill = staticmethod(procs.kill)
    adapters = staticmethod(net.adapters)
    internet = staticmethod(net.internet)
    lan_peers = staticmethod(net.lan_peers)
    removable_drives = staticmethod(devices.removable_drives)
    clipboard_seq = staticmethod(devices.clipboard_seq)
    clipboard_text = staticmethod(devices.clipboard_text)
    close_tab = staticmethod(input.close_tab)
    screenshot = staticmethod(capture.screenshot)
    open_path = staticmethod(_open_path)
