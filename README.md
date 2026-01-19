# Playwright CI/CD Practice Project

This is a practice project to learn Playwright testing with Python and GitHub Actions CI/CD.

## Setup Instructions

### 1. Clone or Create This Project

```bash
mkdir playwright-practice
cd playwright-practice
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Run Tests Locally

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run only smoke tests
pytest -m smoke

# Run specific test file
pytest tests/test_example_basic.py

# Run in headed mode (see browser)
pytest --headed

# Run with HTML report
pytest --html=report.html
```

## CI/CD Setup

### 1. Initialize Git Repository

```bash
git init
git add .
git commit -m "Initial commit with Playwright tests"
```

### 2. Create GitHub Repository

1. Go to GitHub.com
2. Click "New Repository"
3. Name it "playwright-practice"
4. Don't initialize with README (we have one)
5. Click "Create Repository"

### 3. Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/playwright-practice.git
git branch -M main
git push -u origin main
```

### 4. Watch CI/CD Run

1. Go to your repository on GitHub
2. Click the "Actions" tab
3. See your workflow running!
4. Click on the workflow to see detailed logs

## Project Structure

playwright-practice/
├── .github/workflows/    # CI/CD configuration
├── tests/                # Test files
├── requirements.txt      # Python dependencies
├── pytest.ini           # Pytest configuration
└── README.md            # This file


## Test Organization

- `test_example_basic.py` - Simple tests for beginners
- `test_example_advanced.py` - Advanced tests with fixtures and markers

## Markers

- `@pytest.mark.smoke` - Quick sanity tests
- `@pytest.mark.regression` - Full test suite
- `@pytest.mark.search` - Search-related tests
- `@pytest.mark.skip` - Skipped tests

## Debugging

### Local Debugging

```bash
# Run in headed mode to see browser
pytest --headed

# Run with slowmo to see actions
pytest --headed --slowmo 1000

# Enable debug mode
PWDEBUG=1 pytest
```

### CI Debugging

1. Go to failed workflow in GitHub Actions
2. Click on failed step
3. Download artifacts (screenshots, videos, traces)
4. Open traces at https://trace.playwright.dev

## Next Steps

1. ✅ Run tests locally
2. ✅ Push to GitHub
3. ✅ Watch CI/CD run in Actions tab
4. ✅ Make a change and push again
5. ✅ Try making a test fail to see CI catch it
6. ✅ Practice debugging with artifacts

## Resources

- [Playwright Python Docs](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
CI/CD Test
