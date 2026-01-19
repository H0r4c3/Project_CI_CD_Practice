"""
Advanced Playwright Tests for Practice
These tests demonstrate more complex Playwright features.
"""

import pytest
from playwright.sync_api import Page, expect


class TestAdvancedExamples:
    """Advanced test examples with fixtures and markers"""
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup that runs before each test in this class"""
        page.goto("https://www.example.com")
        yield
        # Teardown code would go here if needed
    
    @pytest.mark.smoke
    def test_screenshot_capability(self, page: Page):
        """Test that demonstrates screenshot capture"""
        # Take a screenshot
        screenshot = page.screenshot()
        
        # Verify screenshot was captured
        assert screenshot is not None
        assert len(screenshot) > 0
    
    def test_viewport_size(self, page: Page):
        """Test that verifies viewport dimensions"""
        # Get viewport size
        viewport = page.viewport_size
        
        # Default viewport in Playwright
        assert viewport is not None
        assert viewport["width"] == 1280
        assert viewport["height"] == 720
    
    @pytest.mark.regression
    def test_multiple_elements(self, page: Page):
        """Test finding multiple elements"""
        # Find all paragraph elements
        paragraphs = page.locator("p")
        
        # Verify at least one paragraph exists
        expect(paragraphs).not_to_have_count(0)
    
    def test_element_attributes(self, page: Page):
        """Test reading element attributes"""
        # Find the link (updated to match current example.com)
        link = page.get_by_role("link", name="Learn more")
        
        # Verify href attribute
        expect(link).to_have_attribute("href", "https://iana.org/domains/example")
    
    @pytest.mark.search
    def test_text_content(self, page: Page):
        """Test that page contains specific text"""
        # Check for specific text in the page (updated to match current content)
        expect(page.locator("body")).to_contain_text("Example Domain")
        expect(page.locator("body")).to_contain_text("This domain is for use in documentation examples")


@pytest.mark.skip(reason="Demonstration of intentionally failing test")
class TestFailingExample:
    """This test will fail on purpose to show CI/CD catching failures"""
    
    def test_intentional_failure(self, page: Page):
        """This test fails intentionally to demonstrate CI/CD"""
        page.goto("https://www.example.com")
        
        # This will fail because the title is "Example Domain", not "Wrong Title"
        expect(page).to_have_title("Wrong Title")