import services
from fastapi.responses import (RedirectResponse)
def redirect_to_spotify ():
    redirect_url = services.generate_spotify_auth_url()
    return RedirectResponse(redirect_url)
