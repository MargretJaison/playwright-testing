# #create function here
# import pytest
# def test_username(user_data):
#     assert user_data["username"] == "testuser"
#     assert user_data["password"] == "testpass"

# def test_values():
#      assert 10>5
#      assert 5!=3
#      assert[1,2,3]==[1,2,3]
#      assert "python" in "python playwright"

# #parameterization 
# import pytest

# @pytest.mark.parametrize(
#     "number,expected",
#     [
#         (2, 4),
#         (3, 9),
#         (4, 16),
#     ]
# )
# def test_square(number, expected):
#     assert number * number == expected

# #markers
# @pytest.mark.smoke
# def test_homepagetitle():
#      assert "Home" =="Home"   
# @pytest.mark.regression
# def test_user_status():
#      assert "Active"=="Active"  
# *************************************

#create our first test 
# from playwright.sync_api import expect

# def test_amazon_homepage(page):

#    response = page.goto(

#      "https://www.amazon.com",

#      wait_until="domcontentloaded",

#      timeout=15000

#    )

#    print("Response status:", response.status if response else None)

#    print("Page title: ",repr(page.title()))

#    print("Current URL:", page.url)

#    print("Page content:", page.locator("body").inner_text()[:500])

#    expect(page).to_have_title(

#       "Amazon.com. Spend less. Smile more.", timeout=15000

#    )
#    from playwright.sync_api import expect

# def test_click_button(page):

#     page.goto("https://www.playwrightautomation.com/practice.html")

#     button = page.get_by_role(

#         "button",

#         name="Submit"

#     )

#     expect(button).to_be_visible()

#     button.click()

# from playwright.sync_api import expect

# def test_search_product(page):

#     page.goto("https://www.amazon.com")

#     search_box = page.get_by_role(

#         "searchbox",

#         name = "Search Amazon"

#     )

#     search_box.fill("headphones")

#     search_box.press("Enter")

#     expect(page).to_have_url("https://www.amazon.com/s?k=headphones&ref=nb_sb_noss")

#day 23rd oct 2026

# def test_extract_heading(page):
#     page.goto("https://the-internet.herokuapp.com/")
#     heading=page.locator("h1").inner_text()
#     print(heading)
#     assert heading=="Welcome to the-internet"

# def test_extract_heading(page):
#     page.goto("https://the-internet.herokuapp.com/")
#     heading=page.locator("h2").text_content()
#     print(heading)

# def test_extract_heading(page):
#     page.goto("https://the-internet.herokuapp.com/")
#     links=page.locator("ul li a").all_text_contents()
#     print(links)
#     assert len(links)>0

# def test_extract_heading(page):
#     page.goto("https://the-internet.herokuapp.com/") 
#     href = page.get_by_role("link",name="Subdirectories").get_attribute("href")
#     print(href) 

#Explicit wait using locator.wait_for()
# from playwright.sync_api import expect
# def test_dynamic_loading(page):
#     page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
#     page.get_by_role("button",name="Start").click()
#     heading=page.locator("#finish h4")
#     heading.wait_for(
#         state="visible",
#         timeout=10000
#     )
#     expect(heading).to_have_text("Hello World!")

#waiting for navigation 
# from playwright.sync_api import expect

# def test_wait_for_url(page):
#     page.goto("https://the-internet.herokuapp.com/login")
#     page.locator("#username").fill("tomsmith")
#     page.locator("#password").fill("SuperSecretPassword!")
#     page.get_by_role("button",name="Login").click()
#     page.wait_for_url("**/secure")
#     expect(page).to_have_url("https://the-internet.herokuapp.com/secure")


#################26/10/2026######################

#from playwright.sync_api import Page, expect
# def test_zoom_meeting_registration(page: Page):
#     #Step 1: Open Zoom registration page
#     page.goto("https://ust.zoom.us/meeting/register/wROkcnzOSO2Z7jeg-vMTPA#/registration")
#     #Step 2: Enter First Name
#     page.get_by_label("First Name").fill("Vikas")
#     #Step 3: Enter Last Name
#     page.get_by_label("Last Name").fill("P")
#     #Step 4: Email
#     page.get_by_label("Email Address").fill("vikasp@gmail.com")
#     #Step 5: Enter UST UID
#     page.get_by_label("UST UID").fill("123456")
#     #Step 6: Verify the entered info
#     expect(page.get_by_label("First Name")).to_have_value("Vikas")
#     expect(page.get_by_label("Last Name")).to_have_value("P")
#     expect(page.get_by_label("Email Address")).to_have_value("vikasp@gmail.com")
#     expect(page.get_by_label("UST UID")).to_have_value("123456")
#     #Step 7: Locate the Resigter and Join Button
#     register_button = page.get_by_role("button", name="Register and Join")
#     #Step 8: Verify the button is visible
#     expect(register_button).to_be_visible()



  

from playwright.sync_api import Page, expect
def test_native_dropdown(page):
    # Step 1: Open URL
    page.goto("https://practice.expandtesting.com/dropdown")

    # Step 2: Locate the simple dropdown
    dropdown = page.locator("#dropdown")

    # Step 3: Verify the dropdown is visible or not
    expect(dropdown).to_be_visible()

    # Step 4: Select option using its value
    dropdown.select_option("1")

    # Step 5: Verify selected value
    expect(dropdown).to_have_value("1")

    # Step 6: Select another option
    dropdown.select_option("2")

    # Step 7: Verify new selected value
    expect(dropdown).to_have_value("2")

    print("Dropdown options were selected successfully")


#checkboxes

# from playwright.sync_api import Page, expect

# def test_checkboxes(page: Page):

#     #Step 1: Open the page

#     page.goto("https://practice.expandtesting.com/checkboxes")

#     #Step 2: Locate the first and second checkboxes

#     checkboxes = page.locator('input[type="checkbox"]')

#     first_checkbox = checkboxes.nth(0) #Checkbox 1

#     second_checkbox = checkboxes.nth(1) #Checkbox 2

#     #Step 3: Verify that both checkboxes are visible or not

#     expect(first_checkbox).to_be_visible()

#     expect(second_checkbox).to_be_visible()

#     #Step 4: Select the first checkbox

#     first_checkbox.check()

#     #Step 5: Verify that first checkbox is selected

#     expect(first_checkbox).to_be_checked()

#     #Step 6: Verify the second checkbox is unchecked

#     expect(second_checkbox).to_be_checked()

#     #Step 7: Deselect the first checkbox

#     first_checkbox.uncheck()

#     #Step 8: Verify the final states

#     expect(first_checkbox).not_to_be_checked()

#     expect(second_checkbox).to_be_checked()

#     print("Checkbox selection and deselection tests passed")



#Radio Button
# from playwright.sync_api import expect

# def test_radio_buttons(page):

#     #Step 1: Open radio button URL

#     page.goto("https://practice.expandtesting.com/radio-buttons")

#     #Step 2: Locate Radio buttons using their labels

#     blue_radio = page.get_by_label("Blue")

#     red_radio = page.get_by_label("Red")

#     yellow_radio = page.get_by_label("Yellow")

#     #Step 3: Select Blue radio button

#     blue_radio.check()

#     #Step 4: Verify the Blue is selected

#     expect(blue_radio).to_be_checked()

#     #Step 5: Select Blue radio button

#     red_radio.check()

#     #Step 6: Verify the Red is selected

#     expect(red_radio).to_be_checked()

#     #Step 7: Select Yellow radio button

#     yellow_radio.check()

#     #Step 8: Verify the Yellow is selected

#     expect(yellow_radio).to_be_checked()

#     #Step 9: Verify that Blue is no longer selected

#     expect(blue_radio).not_to_be_checked()

#     #Step 10: Verify that Red is no longer selected

#     expect(red_radio).not_to_be_checked()

#     print("Radio button selection tests passed.")


#multiple tabs in playwright

from playwright.sync_api import Page, expect

def test_multiple_tabs(page: Page):

    #step 1: open first website

    page.goto("https://example.com")

    #Verify the first webpage

    expect(page).to_have_title("Example Domain")

    print("First tab URL: ", page.url)

    #Step 2: Create a second tab in same browser

    second_page = page.context.new_page()

    second_page.goto("https://www.wikipedia.org")

    #Verify the second website

    expect(second_page).to_have_title("Wikipedia")

    print("Second tab URL:", second_page.url)

    #Step 3: Verify the original tab is still open

    expect(page).to_have_title("Example Domain")

    #Step 4: Verify that two pages exist in the context

    all_pages = page.context.pages

    assert len(all_pages) == 2

    print("No.of open pages:", len(all_pages))


#multiple tabs in playwright

def test_multiple_tabs(page:Page):

        page.goto("https://example.com")
    
        #Verify the first webpage
    
        expect(page).to_have_title("Example Domain")
    
        print("First tab URL: ", page.url)
    
        #Step 2: Create a second tab in same browser
    
        second_page = page.context.new_page()
    
        second_page.goto("https://www.wikipedia.org")
    
        #Verify the second website
    
        expect(second_page).to_have_title("Wikipedia")
    
        print("Second tab URL:", second_page.url)
    
        #Step 3: Verify the original tab is still open
    
        expect(page).to_have_title("Example Domain")
    
        #Step 4: Verify that two pages exist in the context
    
        all_pages = page.context.pages
    
        assert len(all_pages) == 2
    
        print("No.of open pages:", len(all_pages))
    
    
        print("Second tab url:",second_page.url)
        #step 3: verify the orginal tab is stil open)
        expect(page).to_have_title("Example Domain")
        #step 4:verify that two pages exist in the context
        all_pages=page.context.pages
        assert len(all_pages)==2
        print("No.of open pages:",len(all_pages))
        #step 5: interact with the second tab
        expect(second_page.get_by_role("heading",name="Wikipedia")).to_be_visible()
        #step 6: close the second tab
        second_page.close()
        #step 7: verify the orginal tab remains open
        expect(page).to_have_title("Example Domain")
        assert len(page.context.pages)==1
        print("multiple tabs test passed successfully")


#Handling a new tab opened by clicking a link

#open the orginal website
#click the link
#capture the  new tab
#verify the new page
#interact with the new page

from pathlib import Path

from playwright.sync_api import expect

def test_new_tab_from_link(page):

    #Step 1: Open the local HTML page

    html_file = Path(__file__).with_name("open_new_tab.html")

    page.goto(html_file.resolve().as_uri())

    #Step 2: Verify the originla page

    expect(

        page.get_by_role("heading", name="Original Page")

    ).to_be_visible()

    #Step 3: Verify thr link exists

    link = page.get_by_role("link", name="Open Example Website in a New Tab")

    expect(link).to_be_visible()

    #Step 4: Click the link and capture new tab

    with page.context.expect_page() as new_page_info:

        link.click()

    new_page = new_page_info.value

    #Step 5:Wait for new tab to finish loading

    new_page.wait_for_load_state("domcontentloaded")

    #Step 6: Verify the new tab URL:

    expect(new_page).to_have_url("https://example.com/")

    print("Oringinal tab URL:", page.url)

    print("New tab URL:", new_page.url)

    #Step 7: Close the new tab

    new_page.close()

    print("New Tab test passed successfully.")