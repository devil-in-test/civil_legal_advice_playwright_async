from playwright.async_api import Page
from models.base_page import BasePage



class CLAYourOutgoingsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    async def navigate(self):
         await self.page.goto("https://checklegalaid.service.gov.uk/outgoings", timeout=5000)

    async def set_rent_amount(self,amount):
         await self.page.get_by_role("group", name="Rent").get_by_label("Amount").click()
         await self.page.get_by_role("group", name="Rent").get_by_label("Amount").fill(amount)

    async def set_rent_frequency(self, frequency):
         await self.page.get_by_role("group", name="Rent").get_by_label("Frequency").select_option(frequency)

    async def set_maintenance_amount(self, amount):
         await self.page.get_by_role("group", name="Maintenance").get_by_label("Amount").click()
         await self.page.get_by_role("group", name="Maintenance").get_by_label("Amount").fill(amount)

    async def set_maintenance_frequency(self,frequency):
         await self.page.get_by_role("group", name="Maintenance").get_by_label("Frequency").select_option(frequency)

    async def set_monthly_income_contribution(self, amount):
         await self.page.get_by_role("textbox", name="Monthly Income Contribution").click()
         await self.page.get_by_role("textbox", name="Monthly Income Contribution").fill(amount)

    async def click_review_answers(self):
         await self.page.get_by_role("button", name="Review your answers").click()