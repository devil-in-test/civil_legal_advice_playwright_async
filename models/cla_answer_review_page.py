from playwright.async_api import Page
from models.base_page import BasePage



class CLAAnswerReviewPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.confirm_button = page.get_by_role("button", name="Confirm")

    async def navigate(self):
            await self.page.goto("https://checklegalaid.service.gov.uk/review", timeout=5000)

    async def click_confirm_button(self):
            await self.confirm_button.click()