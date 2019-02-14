from robot.api import logger  # noqa:  F401 #pylint: disable=unused-import
from TestStack.White.UIItems.ListBoxItems import ComboBox, ListBox
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class ListKeywords(LibraryComponent):
    @keyword
    def select_listbox_value(self, locator, value):
        """Selects a value from a listbox.

        ``locator`` is the locator of the listbox.
        Locator syntax is explained in `Item locators`.

        ``value`` is the value to be selected.
        """
        listbox = self.state._get_typed_item_by_locator(ListBox, locator)
        listbox.Select(value)

    @keyword
    def select_listbox_index(self, locator, item_index):
        """Selects an item by its index from a listbox.

        ``locator`` is the locator of the listbox.
        Locator syntax is explained in `Item locators`.

        ``item_index`` is the index of the item to select.
        """
        listbox = self.state._get_typed_item_by_locator(ListBox, locator)
        listbox.Select(int(item_index))

    @keyword
    def listbox_selection_should_be(self, locator, expected):
        """Checks the listbox selection.

        Fails if the selection was not as expected.

        ``locator`` is the locator of the listbox.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected selection value.
        """
        listbox = self.state._get_typed_item_by_locator(ListBox, locator)
        if listbox.SelectedItemText != expected:
            raise AssertionError("Expected listbox selection to be " +   # noqa: W504
                                 expected + ", was " + listbox.SelectedItemText)

    @keyword
    def select_combobox_value(self, locator, value):
        """Selects a value from a combobox.

        ``locator`` is the locator of the combobox.
        Locator syntax is explained in `Item locators`.

        ``value`` is the value to be selected.
        """
        combobox = self.state._get_typed_item_by_locator(ComboBox, locator)
        combobox.Select(value)

    @keyword
    def select_combobox_index(self, locator, item_index):
        """
        Selects a value from combobox by using its index.

        ``locator`` is the locator of the combobox.
        Locator syntax is explained in `Item locators`.

        ``item_index`` is the index to be selected.
        """
        combobox = self.state._get_typed_item_by_locator(ComboBox, locator)
        combobox.Select(int(item_index))

    @keyword
    def verify_combobox_item(self, locator, expected):
        """*DEPRECATED* Please use Verify Combobox Selection instead
        Verifies the selected value of a combobox.

        ``locator`` is the locator of the combobox.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected selection value.
        """
        self.verify_combobox_selection(locator, expected)

    @keyword
    def verify_combobox_selection(self, locator, expected):
        """Verifies that the combobox value is selected.

        ``locator`` is the locator of the combobox.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected selection value.
        """
        combobox = self.state._get_typed_item_by_locator(ComboBox, locator)
        self.state._verify_value(expected, combobox.EditableText)
