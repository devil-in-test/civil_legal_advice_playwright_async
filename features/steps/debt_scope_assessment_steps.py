import re

from behave.api.async_step import async_run_until_complete
from playwright.async_api import Page,expect

from behave import (given,when,then)


from models.cla_start_page import CLAStartPage
from models.cla_topic_page import CLATopicPage
from models.cla_debt_page import CLADebtPage
from models.cla_is_available_page import CLAIsAvailablePage
from models.cla_about_you_page import CLAAboutYouPage
from models.cla_your_income_page import CLAYourIncomePage
from models.cla_your_outgoings import CLAYourOutgoingsPage
from models.cla_answer_review_page import CLAAnswerReviewPage
from models.cla_eligible_page import CLAEligiblePage
from models.cla_not_eligible_page import CLANotEligiblePage

@given(u'I navigate to the civil legal advice start page')
@async_run_until_complete
async def step_impl(context):
    page = CLAStartPage(context.page)
    await page.navigate()

@given(u'I click start now')
@async_run_until_complete
async def step_impl(context):
    page = CLAStartPage(context.page)
    await page.click_start_now()


@then(u'I am viewing the civil legal advice topic page')
@async_run_until_complete
async def step_impl(context):
    page = CLATopicPage(context.page)
    await expect(page.page).to_have_url(re.compile("/scope/diagnosis/"))


@when(u'I click the debt topic')
@async_run_until_complete
async def step_impl(context):
    page = CLATopicPage(context.page)
    await page.click_debt_topic()

@then(u'I am viewing the civil legal advice debt page')
@async_run_until_complete
async def step_impl(context):
    await expect(context.page).to_have_url(re.compile("n43n2"))


@when(u'I click that I am at risk of losing my home')
@async_run_until_complete
async def step_impl(context):
    page = CLADebtPage(context.page)
    await page.click_at_risk_losing_home()

@then(u'I am viewing the civil legal aid is available for this problem page')
@async_run_until_complete
async def step_impl(context):
    await expect(context.page).to_have_url(re.compile("hlpas=yes"))

@when(u'I click check if I qualify financially')
@async_run_until_complete
async def step_impl(context):
    page = CLAIsAvailablePage(context.page)
    await page.click_check_financial()


@when(u'answer No to Do You have a partner?')
@async_run_until_complete
async def step_impl(context):
    page = CLAAboutYouPage(context.page)
    await page.click_do_you_have_a_partner_no()


@when(u'answer No to Do you receive any benefits (including Child Benefit)?')
@async_run_until_complete
async def step_impl(context):
    page = CLAAboutYouPage(context.page)
    await page.click_do_you_receive_benefits_no()

@when(u'answer No to Do you have any children aged 15 or under?')
@async_run_until_complete
async def step_impl(context):
    page = CLAAboutYouPage(context.page)
    await page.click_do_you_have_children_under_15_no()

@when(u'answer No to Do you have any dependants aged 16 or over?')
@async_run_until_complete
async def step_impl(context):
    page = CLAAboutYouPage(context.page)
    await page.click_have_dependent_children_over_16_no()

@when(u'answer No to Do you own any property?')
@async_run_until_complete
async def step_impl(context):
    page = CLAAboutYouPage(context.page)
    await page.click_do_you_own_a_property_no()


@when(u'answer No to Are you employed?')
@async_run_until_complete
async def step_impl(context):
    page = CLAAboutYouPage(context.page)
    await page.click_are_you_employed_no()


@when(u'answer No to Are you self-employed?')
@async_run_until_complete
async def step_impl(context):
    page = CLAAboutYouPage(context.page)
    await page.click_are_you_self_employed_no()


@when(u'answer No to Are you or your partner (if you have one) aged 60 or over?')
@async_run_until_complete
async def step_impl(context):
    page = CLAAboutYouPage(context.page)
    await page.click_are_you_or_your_partner_over_60_no()

@when(u'answer No to Do you have any savings or investments?')
@async_run_until_complete
async def step_impl(context):
    page = CLAAboutYouPage(context.page)
    await page.click_do_you_have_savings_or_investments_no()

@when(u'answer No to Do you have any valuable items worth over £500 each?')
@async_run_until_complete
async def step_impl(context):
    page = CLAAboutYouPage(context.page)
    await page.click_do_you_have_valuables_worth_over_500_pounds_each_no()

@when(u'I click continue to Your money coming in page')
@async_run_until_complete
async def step_impl(context):
    page = CLAAboutYouPage(context.page)
    await page.click_continue_button()


@when(u'answer {amount} to your maintenance received')
@async_run_until_complete
async def step_impl(context, amount):
    page = CLAYourIncomePage(context.page)
    await page.set_maintenance_received_amount(amount)


@when(u'answer {frequency} to your maintenance frequency')
@async_run_until_complete
async def step_impl(context,frequency):
    page = CLAYourIncomePage(context.page)
    await page.set_maintenance_received_frequency(frequency)


@when(u'answer {amount} to your pension received')
@async_run_until_complete
async def step_impl(context,amount):
    page = CLAYourIncomePage(context.page)
    await page.set_pension_received_amount(amount)


@when(u'answer {frequency} to your pension frequency')
@async_run_until_complete
async def step_impl(context,frequency):
    page = CLAYourIncomePage(context.page)
    await page.set_pension_received_frequency(frequency)


@when(u'answer {amount} to your other income')
@async_run_until_complete
async def step_impl(context,amount):
    page = CLAYourIncomePage(context.page)
    await page.set_other_income_amount(amount)


@when(u'answer {frequency} to your other income frequency')
@async_run_until_complete
async def step_impl(context,frequency):
    page = CLAYourIncomePage(context.page)
    await page.set_other_income_frequency(frequency)


@when(u'I click continue to Your outgoings page')
@async_run_until_complete
async def step_impl(context):
    page = CLAYourIncomePage(context.page)
    await page.click_continue_button()


@when(u'answer {amount} to your rent amount')
@async_run_until_complete
async def step_impl(context,amount):
    page = CLAYourOutgoingsPage(context.page)
    await page.set_rent_amount(amount)


@when(u'answer {frequency} to your rent schedule')
@async_run_until_complete
async def step_impl(context,frequency):
    page = CLAYourOutgoingsPage(context.page)
    await page.set_rent_frequency(frequency)


@when(u'answer {amount} to your maintenance payment')
@async_run_until_complete
async def step_impl(context,amount):
    page = CLAYourOutgoingsPage(context.page)
    await page.set_maintenance_amount(amount)


@when(u'answer {frequency} to your maintenance payment schedule')
@async_run_until_complete
async def step_impl(context,frequency):
    page = CLAYourOutgoingsPage(context.page)
    await page.set_maintenance_frequency(frequency)

@when(u'answer {amount} to your monthly income contribution order')
@async_run_until_complete
async def step_impl(context,amount):
    page = CLAYourOutgoingsPage(context.page)
    await page.set_monthly_income_contribution(amount)

@when(u'I click continue to review the answers page')
@async_run_until_complete
async def step_impl(context):
    page = CLAYourOutgoingsPage(context.page)
    await page.click_review_answers()


@when(u'I click reviewed answers')
@async_run_until_complete
async def step_impl(context):
    page = CLAAnswerReviewPage(context.page)
    await page.click_confirm_button()


@then(u'I get confirmed my eligibility is {eligibility}')
@async_run_until_complete
async def step_impl(context,eligibility):
    if eligibility == 'eligible':
        await expect(context.page).to_have_url(re.compile("/result/eligible"))
    else:
        page = CLAEligiblePage(context.page)
        await expect(context.page).to_have_url(re.compile("/result/hlpas"))

