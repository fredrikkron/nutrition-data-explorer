import taipy.gui.builder as tgb

with tgb.Page() as home_page:
    with tgb.part(class_name="container-card"):
        tgb.navbar()
        
        with tgb.part():
            tgb.text("# Näringsportalen", mode="md")

        with tgb.part():
            tgb.text(
            """
            Välkommen till Näringsportalen!

            Detta är en interaktiv webbapplikation som låter dig utforska och analysera näringsdata på ett enkelt och intuitivt sätt.

            Använd navigeringsfältet ovan för att komma åt olika sektioner av applikationen, inklusive instrumentpanelen och diagrammen.
            
            """
            , mode="md"
        )