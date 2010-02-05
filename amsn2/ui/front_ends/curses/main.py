
from amsn2.ui import base
import command

import curses
class aMSNMainWindow(base.aMSNMainWindow):
    def __init__(self, amsn_core):
        self._amsn_core = amsn_core

    def show(self):
        self._stdscr = curses.initscr()
        self._command_line = command.CommandLine(self._stdscr, None)
        self.__init_colors()
        curses.noecho()
        curses.cbreak()
        self._stdscr.keypad(1)
        self._stdscr.box()
        self._stdscr.refresh()
        self._amsn_core.idler_add(self.__on_show)

    def hide(self):
        curses.nocbreak()
        self._stdscr.keypad(0)
        curses.echo()
        curses.endwin()

    def __on_show(self):
        self._amsn_core.main_window_shown()

    def set_title(self,title):
        self._title = title

    def set_menu(self,menu):
        pass

    def setFocusedWindow(self, window):
        self._command_line.setCharCb(window._on_char_cb)

    def __init_colors(self):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)

