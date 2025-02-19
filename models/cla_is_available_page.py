from playwright.async_api import Page
from models.base_page import BasePage


class CLAIsAvailablePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.check_financial_button = page.get_by_role('button', name='Check if you qualify financially')

    async def navigate(self):
            await self.page.goto("https://checklegalaid.service.gov.uk/legal-aid-available?hlpas=yes", timeout=5000)

    async def click_check_financial(self):
            await self.check_financial_button.click()