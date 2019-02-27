from TestStack.White import AutomationException, Desktop
from TestStack.White.Configuration import CoreAppXmlConfiguration
from TestStack.White.Factory import InitializeOption  # noqa: E402
from TestStack.White.UIItems.Finders import SearchCriteria  # noqa: E402
from TestStack.White.UIItems.WindowItems import Window  # noqa: F401
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from robot.api import logger  # noqa: F401

WINDOW_STRATEGIES = {"id": "ByAutomationId",
                     "class_name": "ByClassName"}


class WindowKeywords(LibraryComponent):
    @keyword
    def attach_window(self, locator):
        """Attaches WhiteLibrary to a window.

        ``locator`` is the locator of the window or a window object.

        === Window locator syntax ===
        Syntax for a window locator is ``prefix:value``.

        When the locator syntax is used, the window is searched from the currently attached application.
        See `Attach Application By Id`, `Attach Application By Name` or
        `Launch application` for more details about attaching an application.

        The following window locators are available:
        | = Prefix =           | = Description =         |
        | title (or no prefix) | Search by the exact window title. If no prefix is given, the window is searched by title by default. |
        | id                   | Search by AutomationID. |
        | class_name           | Search by class name.   |

        === Window objects ===
        A window can also be attached by directly passing the window object as the ``locator`` parameter value.

        Example:
        | @{windows} | `Get Application Windows` | |
        | Attach Window | ${windows[1]} | # attach window at index 1 in window list |
        """
        self.state.window = self._get_window(locator)

    @keyword
    def close_window(self, locator=None):
        """Closes a window.

        ``locator`` is the locator of the window or a window object (optional).

        If no ``locator`` value is given, the currently attached window is closed.
        See `Attach Window` for details about window locators and attaching a window.
        """
        if locator is not None:
            window = self._get_window(locator)
            window.Close()
        else:
            self.state.window.Close()

    @keyword
    def get_application_windows(self):
        """Returns a list of windows belonging to the currently attached application.

        Assumes that an application is attached.
        See `Attach Application By Name` and `Attach Application By Id` for details.
        """
        return list(self.state.app.GetWindows())

    @keyword
    def get_desktop_windows(self):
        """Returns a list of windows on the desktop."""
        return list(Desktop.Instance.Windows())

    @keyword
    def select_modal_window(self, window_title):
        """Select modal window.

        ``window_title`` is the title of the window.
        """
        self.state.window = self.state.window.ModalWindow(window_title)

    @keyword
    def get_window_title(self):
        """Returns title of the currently attached window.

        Assumes that a window is attached. See `Attach Window` for details.
        """
        return self.state.window.Title

    @keyword
    def window_title_should_be(self, expected):
        """Verifies that the title of the currently attached window is ``expected``.

        Assumes that a window is attached. See `Attach Window` for details."""
        self.state._verify_string_value(expected, self.state.window.Title)

    @keyword
    def window_title_should_contain(self, expected):
        """Verifies that the title of the currently attached window contains text ``expected``.

        Assumes that a window is attached. See `Attach Window` for details."""
        self.state._contains_string_value(expected, self.state.window.Title)

    def _get_window(self, locator):
        if isinstance(locator, Window):
            return locator
        return self._get_window_by_locator(locator)

    def _get_window_by_locator(self, locator):
        search_strategy, locator_value = self._parse_window_locator(locator)
        try:
            if search_strategy == "title":
                return self.state.app.GetWindow(locator_value)
            search_criteria = getattr(SearchCriteria, WINDOW_STRATEGIES[search_strategy])(locator_value)
            return self.state.app.GetWindow(search_criteria, InitializeOption.NoCache)
        except KeyError:
            raise ValueError("'{}' is not a valid locator prefix for a window".format(search_strategy))
        except AttributeError as error_msg:
            error_msg = str(error_msg)
            if "NoneType" in error_msg:
                error_msg = "No application attached."
            raise AttributeError(error_msg)
        except AutomationException as error_msg:
            error_msg = str(error_msg)
            replaced_text = "after waiting for {0} seconds".format(
                CoreAppXmlConfiguration.Instance.FindWindowTimeout / 1000)
            raise AutomationException(error_msg.replace("after waiting for 30 seconds", replaced_text), "")

    def _parse_window_locator(self, locator):
        if ":" not in locator:
            locator = "title:" + locator
        idx = locator.index(":")
        return locator[:idx], locator[(idx + 1):]
