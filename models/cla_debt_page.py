from playwright.async_api import Page
from models.base_page import BasePage


class CLADebtPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.at_risk_losing_home_button = page.get_by_role("button", name="mortgage debt or repossession")

    async def navigate(self):
             await self.page.goto("https://checklegalaid.service.gov.uk/scope/diagnosis/n43n2", timeout=5000)

    async def click_at_risk_losing_home(self):
            await self.at_risk_losing_home_button.click()