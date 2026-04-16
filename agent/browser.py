from playwright.sync_api import sync_playwright

def run_browser_task(url: str, task: str = "", data: dict = {}):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        page.goto(url)
        page.wait_for_timeout(2000)

        if "create" in task.lower():
            page.fill("#username", data.get("name", "Test User"))
            page.fill("#email", data.get("email", "test@test.com"))
            page.fill("#role", data.get("role", "User"))
            page.click("button")
            page.wait_for_timeout(3000)

        elif "reset" in task.lower():
            page.fill("#email", data.get("email", "test@test.com"))
            page.fill("#newpass", data.get("password", "NewPass123"))
            page.click("button")
            page.wait_for_timeout(3000)

        elif "list" in task.lower() or "users" in task.lower():
            page.wait_for_timeout(3000)

        browser.close()
        return f"Task done: {task}"