from taipy.gui import Gui
from frontend.dashboard import dashboard_page

pages = {"dashboard": dashboard_page} 

if __name__ == "__main__":
    Gui(pages=pages, css_file="assets/styling.css").run(
        use_reloader=True, port=8080
    )