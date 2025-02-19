from playwright.async_api import Page
from models.base_page import BasePage



class CLANotEligiblePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    async def navigate(self):
        await self.page.goto("https://checklegalaid.service.gov.uk/result/not-eligible", timeout=5000)