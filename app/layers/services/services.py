from ..transport.transport import getAllImages as getAllImagesTransport
from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user
import random


def getAllImages():
    for image in images:
        images = getAllImagesTransport()  # Llamada al transport layer para obtener los datos
        cards=[]
        card = crearCard(image)  # Usar una función auxiliar para estructurar la card
        cards.append(card)

    # Paso 3: Retornar el listado de cards generadas
    return cards


def crearCard(image):
    """
    Convierte un objeto de imagen en una card. Si existen nombres alternativos, selecciona uno al azar.
    """
    # Extracción de datos básicos con valores por defecto si no existen
    name = image.get("name", "Sin nombre")
    id = image.get("id", "Sin ID")
    alternate_names = image.get("alternate_names", [])
    
    # Selección de un nombre alternativo o mensaje en caso de no haber ninguno
    if alternate_names:
        alternate_name = random.choice(alternate_names)
    else:
        alternate_name = "No hay nombres alternativos disponibles"

    # Estructura de la card
    return {
        "id": id,
        "name": name,
        "alternate_name": alternate_name,
    }



















# función que filtra según el nombre del personaje.
def filterByCharacter(name):
    filtered_cards = []

    for card in getAllImages():
        # debe verificar si el name está contenido en el nombre de la card, antes de agregarlo al listado de filtered_cards.
        filtered_cards.append(card)

    return filtered_cards

# función que filtra las cards según su casa.
def filterByHouse(house_name):
    filtered_cards = []

    for card in getAllImages():
        # debe verificar si la casa de la card coincide con la recibida por parámetro. Si es así, se añade al listado de filtered_cards.
        filtered_cards.append(card)

    return filtered_cards

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request en una Card (ver translator.py)
    fav.user = get_user(request) # le asignamos el usuario correspondiente.

    return repositories.save_favourite(fav) # lo guardamos en la BD.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS Los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # convertimos cada favorito en una Card, y lo almacenamos en el listado de mapped_favourites que luego se retorna.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.delete_favourite(favId) # borramos un favorito por su ID


