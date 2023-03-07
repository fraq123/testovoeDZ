from selenium.webdriver.common.by import By


class CheckBoxPageLocators:
    HOME_BUTTON = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-expand-close"]')
    DOWNLOADS_BUTTON = (By.CSS_SELECTOR, 'li:nth-child(3) span button svg')
    WORLD_FILE = (By.CSS_SELECTOR, 'label[for="tree-node-wordFile"]')
    RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')