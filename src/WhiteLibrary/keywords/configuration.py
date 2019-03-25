from robot.api import logger
from robot.utils import timestr_to_secs
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from Castle.Core.Logging import LoggerLevel
from TestStack.White.Configuration import CoreAppXmlConfiguration, WhiteDefaultLoggerFactory


class WhiteConfigurationKeywords(LibraryComponent):
    @keyword
    def set_white_log_level(self, level):
        """Sets log level for White's console log.

        Valid ``level`` values are ``INFO``, ``WARN`` and ``DEBUG`` (case insensitive).
        Default log level is ``INFO``.
        """
        level = level.upper()
        if level == "INFO":
            CoreAppXmlConfiguration.Instance.LoggerFactory = WhiteDefaultLoggerFactory(LoggerLevel.Info)
        elif level == "WARN":
            CoreAppXmlConfiguration.Instance.LoggerFactory = WhiteDefaultLoggerFactory(LoggerLevel.Warn)
        elif level == "DEBUG":
            CoreAppXmlConfiguration.Instance.LoggerFactory = WhiteDefaultLoggerFactory(LoggerLevel.Debug)
        else:
            raise ValueError("Invalid log level: '{}'".format(level))

    @keyword
    def set_white_busy_timeout(self, timeout):
        """Sets BusyTimeout for White and returns original value.

        ``timeout`` is the timeout value as Robot time string.

         Default timeout is 5 seconds.
        """
        CoreAppXmlConfiguration.Instance.BusyTimeout = self._get_timestr_in_milliseconds(timeout)
        logger.info("White Busy Timeout set to " + str(CoreAppXmlConfiguration.Instance.BusyTimeout))
        return self._get_milliseconds_as_timestr(CoreAppXmlConfiguration.Instance.BusyTimeout)

    @keyword
    def get_white_busy_timeout(self):
        """Returns BusyTimeout value of White.

        See also `Set White Busy Timeout`.
        """
        return self._get_milliseconds_as_timestr(CoreAppXmlConfiguration.Instance.BusyTimeout)

    @keyword
    def set_white_find_window_timeout(self, timeout):
        """Sets FindWindowTimeout for White and returns original value.

        ``timeout`` is the timeout value as Robot time string.

        Default timeout is 30 seconds.
        """
        CoreAppXmlConfiguration.Instance.FindWindowTimeout = self._get_timestr_in_milliseconds(timeout)
        logger.info("White FindWindowTimeout set to " + str(CoreAppXmlConfiguration.Instance.FindWindowTimeout))
        return self._get_milliseconds_as_timestr(CoreAppXmlConfiguration.Instance.FindWindowTimeout)

    @keyword
    def get_white_find_window_timeout(self):
        """Returns FindWindowTimeout value of White.

        See also `Set White Find Window Timeout`.
        """
        return self._get_milliseconds_as_timestr(CoreAppXmlConfiguration.Instance.FindWindowTimeout)

    @keyword
    def set_white_double_click_interval(self, interval):
        """Sets DoubleClickInterval for White and returns original value.

        DoubleClickInterval adds delay in double click action between clicks.

        ``interval`` is the interval value as Robot time string.

        Default interval is 0 milliseconds.
        """
        CoreAppXmlConfiguration.Instance.DoubleClickInterval = self._get_timestr_in_milliseconds(interval)
        logger.info("White DoubleClickInterval set to " + str(CoreAppXmlConfiguration.Instance.DoubleClickInterval))
        return self._get_milliseconds_as_timestr(CoreAppXmlConfiguration.Instance.DoubleClickInterval)

    @keyword
    def get_white_double_click_interval(self):
        """Returns DoubleClickInterval value of White.

        See also `Set White Double Click Interval`.
        """
        return self._get_milliseconds_as_timestr(CoreAppXmlConfiguration.Instance.DoubleClickInterval)

    @keyword
    def set_white_drag_step_count(self, value):  # pylint: disable=no-self-use
        """Sets DragStepCount for White

        ``value`` is the DragStepCount value as integer.

        DragStepCount defines how many steps White uses to move dragged object to the destination.
        With default value 1 the dragged object is moved instantly in a single step from start to destination.
        """
        CoreAppXmlConfiguration.Instance.DragStepCount = int(value)
        logger.info("White DragStepCount set to" + str(CoreAppXmlConfiguration.Instance.DragStepCount))
        return CoreAppXmlConfiguration.Instance.DragStepCount

    @keyword
    def get_white_drag_step_count(self):  # pylint: disable=no-self-use
        """Returns DragStepCount value of White.

        See also `Set White Drag Step Count`.
        """
        return CoreAppXmlConfiguration.Instance.DragStepCount

    def _get_timestr_in_milliseconds(self, time_string):  # pylint: disable=no-self-use
        return timestr_to_secs(time_string) * 1000

    def _get_milliseconds_as_timestr(self, milliseconds):  # pylint: disable=no-self-use
        return "{} milliseconds".format(milliseconds)
