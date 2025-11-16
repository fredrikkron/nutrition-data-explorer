import taipy.gui.builder as tgb

with tgb.Page() as dashboard_page:
    with tgb.part(class_name="container-card"):
        tgb.navbar()