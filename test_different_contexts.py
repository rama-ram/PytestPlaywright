from playwright.sync_api import Page, expect

def test_page_context(page: Page):
    page.goto("https://example.com")
    page.get_by_role("link",name="More information").click()
    expect(page.get_by_text ("IANA-managed Reserved Domains")).to_be_visible()

