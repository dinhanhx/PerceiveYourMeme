# An easter egg
import urllib3
from PIL import Image
from io import BytesIO
try:
    from .CONST import HEADERS
except ImportError:
    from CONST import HEADERS

# I intentionally do this in one line.
url = 'https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/0/03/Pym_Particles.png'
Image.open(BytesIO(urllib3.PoolManager().request('GET',url,headers=HEADERS).data)).show()
