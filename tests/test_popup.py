from pathlib import Path
from playwright.sync_api import expect

def test_popup_window(page):
    #step1:open the local popup practice html code
    html_file=Path(__file__).with_name("popup_practice.html")
    page.goto(html_file.rrsolve().as_url())

    #step 2 verify the orginal page
    expect(page.get_by_role(
        "heading",name="Popup Window Practice"
    )).to_be_visible()

    #step 3:Register popup expectation before clicking
    with page.expect_popup() as popup_info:
        page.get_by_role("button",name="open popup").click()

    #step 4:Capture the popup page
    popup=popup_info.value

    #step 5: verify the popup content
    expect(popup).to_have_url("https://example.com/")

    #step 6:Verify the popup content
    expect(popup.get_by_role("heading",name="Example Domain")).to_be_visible()
    print("Popup URL:",popup.url)
    print("Popup title:",popup.title())

    #step 7:Verify whether orginal page is still open or not
    # 
    expect(page.get_by_role("heading",name="Popup window practice")).to_be_visible()
    popup.close()
    print("Popup test passed successfully")    

    