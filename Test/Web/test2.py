from Pages.addtocart import AddToCartPage
import pytest


class Test_AtidStore(AddToCartPage):
    def obj(self):
        addtocart = AddToCartPage()
        return addtocart

    def test_accessories_link(self):
        self.obj().open()
        self.obj().execute_accessories()

    def test_stor_link(self):
        self.obj().open()
        self.obj().execute_store()

    def test_men_link(self):
        self.obj().open()
        self.obj().execute_men()

    def test_woment_link(self):
        self.obj().open()
        self.obj().execute_women()

    def test_comment(self):
        self.obj().open()
        self.obj().execute_comment()

    def test_end_to_end_login(self):
        self.obj().open()
        self.obj().execute_e2e_login()

    def test_end_to_end_register(self):
        self.obj().open()
        self.obj().execute_e2e_register()

    def test_add_all(self):
        self.obj().open()
        self.obj().execute_add_all()

    def test_5star(self):
        self.obj().open()
        self.obj().execute_5star()

