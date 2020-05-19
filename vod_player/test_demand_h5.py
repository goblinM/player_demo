# -*- encoding=utf-8 -*-
"""
点播h5
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from config import location_chrome
from data_layout.url_yaml import YamlMethods
import logging
logging.basicConfig(level=logging.INFO)


class TestSuite(object):
    chromeOpitons = Options()
    prefs = {
        "profile.managed_default_content_settings.images":
            1,
        "profile.content_settings.plugin_whitelist.adobe-flash-player":
            1,
        "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player":
            1,
    }
    chromeOpitons.add_experimental_option('prefs', prefs)
    chromeOpitons.add_argument("--use-fake-ui-for-media-stream=1")
    chromeOpitons.binary_location = location_chrome
    driver = webdriver.Chrome(chrome_options=chromeOpitons)
    url_data = YamlMethods().single_yaml_load()
    url_data = url_data.get("demand_h5_test")
    player_version = None

    def test_close_driver(self):
        self.driver.quit()

    def test_preview(self):
        """预览测试 ok"""
        encrypted_url = self.url_data.get("encrypted_url")
        # PreviewTest().browser_test(self.driver, "Chrome", encrypted_url)







