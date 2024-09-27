from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set the path to your WebDriver

driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the jQuery UI Droppable page
    driver.get("https://jqueryui.com/droppable/")

    # Allow time for the page to load
    time.sleep(3)

    # Step 2: Switch to the iframe that contains the droppable elements
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

    # Step 3: Locate the draggable and droppable elements
    draggable = driver.find_element(By.ID, "draggable")
    droppable = driver.find_element(By.ID, "droppable")

    # Step 4: Perform drag and drop using Action Chains
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, droppable).perform()

    # Optional: Add a delay to observe the action
    time.sleep(2)

    # Optional: Verify the drop by checking the text of the droppable area
    dropped_text = droppable.text
    print("Dropped Text:", dropped_text)

finally:
    # Close the browser
    driver.quit()
