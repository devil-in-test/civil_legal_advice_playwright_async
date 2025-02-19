from playwright.async_api import Page
from models.base_page import BasePage



class CLAYourIncomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.continue_button = page.get_by_role("button", name="Continue")
        self.maintenance_received_amount_input = page.locator("#your_income-maintenance-per_interval_value")
        self.maintenance_received_amount_frequency_select = page.locator("#your_income-maintenance-interval_period")
        self.your_income_pension_per_interval_input =page.locator("#your_income-pension-per_interval_value")
        self.your_income_pension_per_interval_frequency = page.locator("#your_income-pension-interval_period")
        self.your_income_other_income_per_interval_value = page.locator("#your_income-other_income-per_interval_value")
        self.your_income_other_income_per_interval_frequency = page.locator("#your_income-other_income-interval_period")

    async def navigate(self):
         await self.page.goto("https://checklegalaid.service.gov.uk/income", timeout=15000)

    async def click_continue_button(self):
         await self.continue_button.click()

    async def set_maintenance_received_amount(self,amount):
         await self.maintenance_received_amount_input.click()
         await self.maintenance_received_amount_input.fill(amount)

    async def set_maintenance_received_frequency(self,frequency):
         await self.maintenance_received_amount_frequency_select.select_option(frequency)

    async def set_pension_received_amount(self,amount):
         await self.your_income_pension_per_interval_input.click()
         await self.your_income_pension_per_interval_input.fill(amount)

    async def set_pension_received_frequency(self,frequency):
         await self.your_income_pension_per_interval_frequency.select_option(frequency)

    async def set_other_income_amount(self,amount):
         await self.your_income_other_income_per_interval_value.click()
         await self.your_income_other_income_per_interval_value.fill(amount)

    async def set_other_income_frequency(self,frequency):
         await self.your_income_other_income_per_interval_frequency.select_option(frequency)