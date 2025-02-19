from playwright.async_api import Page
from models.base_page import BasePage


class CLAAboutYouPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.continue_button = page.get_by_role("button", name="Continue")
        self.have_partner_no_radio = page.locator("#have_partner-1")


    async def navigate(self):
        await self.page.goto("https://checklegalaid.service.gov.uk/about", timeout=5000)


    async def click_continue_button(self):
        await self.continue_button.click()


    async def click_do_you_have_a_partner_no(self):
        await self.have_partner_no_radio.check()


    async def click_do_you_receive_benefits_no(self):
        await self.page.get_by_role("group", name="Do you receive any benefits (").get_by_label("No").check()


    async def click_do_you_have_children_under_15_no(self):
        await self.page.get_by_role("group", name="Do you have any children aged").get_by_label("No").check()


    async def click_have_dependent_children_over_16_no(self):
        await self.page.get_by_role("group", name="Do you have any dependants").get_by_label("No").check()


    async def click_do_you_own_a_property_no(self):
        await self.page.get_by_role("group", name="Do you own any property?").get_by_label("No").check()


    async def click_are_you_employed_no(self):
        await self.page.get_by_role("group", name="Are you employed?").get_by_label("No").check()


    async def click_are_you_self_employed_no(self):
        await self.page.get_by_role("group", name="Are you self-employed?").get_by_label("No").check()


    async def click_are_you_or_your_partner_over_60_no(self):
        await self.page.get_by_role("group", name="Are you or your partner (if").get_by_label("No").check()


    async def click_do_you_have_savings_or_investments_no(self):
        await self.page.get_by_role("group", name="Do you have any savings or").get_by_label("No").check()


    async def click_do_you_have_valuables_worth_over_500_pounds_each_no(self):
        await self.page.get_by_role("group", name="Do you have any valuable").get_by_label("No").check()
