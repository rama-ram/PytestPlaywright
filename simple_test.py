import re
from playwright.sync_api import Page, expect

def test_navigation(page: Page):
    page.goto("https://playwright.dev/")
    page.pause()
    expect(page).to_have_title(re.compile("Playwright"))


def test_perform_action(page: Page):
    page.goto("https://playwright.dev/")
    page.pause()
    expect(page).to_have_title(re.compile("Playwright"))
    page.get_by_role("link",name="Get Started").click()
    expect(page).to_have_title(re.compile("Installation"))