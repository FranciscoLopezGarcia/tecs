from .air_downloader import get_air
from .infoandina_downloader import get_infoandina

# Here is where new modules should be added in order to the app to be aware of them
DOWNLOADERS = {
    "air": get_air,
    "infoandina": get_infoandina
}