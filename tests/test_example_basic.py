"""
Basic Playwright Tests for Practice
These tests demonstrate simple Playwright operations.
"""

import pytest
from playwright.sync_api import Page, expect


class TestBasicExamples:
    """Basic test examples to verify Playwright setup"""
    
    def test_page_loads(self, page: Page):
        """Test that a page loads successfully"""
        # Navigate to the page
        page.goto("https://www.example.com")
        
        # Verify the page title
        expect(page).to_have_title("Example Domain")
        
        # Verify page loaded
        assert page.url == "https://www.example.com/"
    
    def test_page_contains_heading(self, page: Page):
        """Test that the page has expected heading"""
        page.goto("https://www.example.com")
        
        # Find heading element
        heading = page.locator("h1")
        
        # Verify heading text
        expect(heading).to_have_text("Example Domain")
    
    def test_page_has_link(self, page: Page):
        """Test that a link exists on the page"""
        page.goto("https://www.example.com")
        
        # Find the link (updated text)
        more_info_link = page.get_by_role("link", name="Learn more")
        
        # Verify link is visible
        expect(more_info_link).to_be_visible()
    
    @pytest.mark.smoke
    def test_navigation(self, page: Page):
        """Test basic navigation functionality"""
        # Go to example.com
        page.goto("https://www.example.com")
        
        # Click the "Learn more" link (updated text)
        page.get_by_role("link", name="Learn more").click()
        
        # Verify we navigated to IANA page
        expect(page).to_have_url("https://www.iana.org/help/example-domains")
        
        # Go back
        page.go_back()
        
        # Verify we're back at example.com
        expect(page).to_have_url("https://www.example.com/")