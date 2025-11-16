from taipy.gui import Gui
from frontend.home import home_page
from frontend.dashboard import dashboard_page

pages = {"home": home_page, "dashboard": dashboard_page}

if __name__ == "__main__":
    Gui(pages=pages).run(
        use_reloader=True, port=8080
    )