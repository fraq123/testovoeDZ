from pages.elements_page import CheckBoxPage


class TestCheckBox:
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        result = check_box_page.check_world_file()
        assert result == 'wordFile', 'checkboxes have not ben selected'
