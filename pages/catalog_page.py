class CatalogPage:
    def __init__(self,page):
        self.page=page
        self.bluetooth_speaker= page.get_by_test_id("product-name-4")


    def open_bluetooth_speaker(self):
        self.bluetooth_speaker.click()

        