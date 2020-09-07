# An easter egg
import urllib3
from CONST import HEADERS
from PIL import Image
from io import BytesIO

# I intentionally do this in one line.
url = 'https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/0/03/Pym_Particles.png'
Image.open(BytesIO(urllib3.PoolManager().request('GET',url,headers=HEADERS).data)).show()
