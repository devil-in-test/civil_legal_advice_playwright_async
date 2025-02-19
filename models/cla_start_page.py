from playwright.async_api import Page
from models.base_page import BasePage


class CLAStartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    async def navigate(self):
        await self.page.goto("https://www.gov.uk/check-legal-aid", timeout=5000)

    async def click_start_now(self):
        await self.page.get_by_role("button", name="Start now").click()