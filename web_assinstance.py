import webbrowser
from datetime import datetime, timedelta
from General_Utilities.fecha import BatchID


fecha = BatchID(
    datetime.now() - timedelta(days=98)
)

# https://www.biblegateway.com/passage/?search=proverbios+3%3A5-6&version=RVR1960
bible = 'https://www.biblegateway.com/versions/Reina-Valera-1960-RVR1960-Biblia/'
labuenasemilla = f'https://labuenasemilla.net/{fecha}'

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(labuenasemilla)
webbrowser.open_new_tab(bible)

