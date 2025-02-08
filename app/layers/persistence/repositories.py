# capa DAO de acceso/persistencia de datos.

from sqlite3 import IntegrityError
from app.models import Favourite

## capa DAO de acceso/persistencia de datos. 
# ---------------------Guarda un Favorito en la Base de datos#------------------------------

from sqlite3 import IntegrityError
from app.models import Favourite

#usa Save_Favorite para insertar un nuevo favorito en la base de datos, se llenan todos los campos con los datos FAV.
#Retorna el objeto guardado FAV
def save_favourite(fav):
    try:
        fav = Favourite.objects.create(
            name=fav.name,  # Nombre del personaje
            gender=fav.gender,  # Género
            house=fav.house,  # Casa
            actor=fav.actor,  # Actor
            image=fav.image,  # Imagen
            
            user=fav.user  # Usuario autenticado
        )
        return fav
    except IntegrityError as e:
        print(f"Error de integridad al guardar el favorito: {e}")
        return None
    except KeyError as e:
        print(f"Error de datos al guardar el favorito: Falta el campo {e}")
        return None


def get_all_favourites(user):
    return list(Favourite.objects.filter(user=user).values(
        'id', 'name', 'gender', 'house', 'actor', 'image'
    ))


def delete_favourite(fav_id):
    try:
        favourite = Favourite.objects.get(id=fav_id)
        favourite.delete()
        return True
    except Favourite.DoesNotExist:
        print(f"El favorito con ID {fav_id} no existe o no pertenece al usuario.")
        return False
    except Exception as e:
        print(f"Error al eliminar el favorito: {e}")
        return False
def save_favourite(fav):
    try:
        fav = Favourite.objects.create(
            name=fav.name,  # Nombre del personaje
            gender=fav.gender,  # Género
            house=fav.house,  # Casa
            actor=fav.actor,  # Actor
            image=fav.image,  # Imagen
            
            user=fav.user  # Usuario autenticado
        )
        return fav
    except IntegrityError as e:
        print(f"Error de integridad al guardar el favorito: {e}")
        return None
    except KeyError as e:
        print(f"Error de datos al guardar el favorito: Falta el campo {e}")
        return None

#Esta función obtiene todos los favoritos de un usuario específico.
# Filtra la tabla Favourite para obtener solo los registros del usuario especificado
# Devuelve una lista con los favoritos del usuario.
def get_all_favourites(user):
    return list(Favourite.objects.filter(user=user).values(
        'id', 'name', 'gender', 'house', 'actor', 'image'
    ))


def delete_favourite(fav_id):
    try:
        favourite = Favourite.objects.get(id=fav_id)
        favourite.delete()
        return True
    except Favourite.DoesNotExist:
        print(f"El favorito con ID {fav_id} no existe o no pertenece al usuario.")
        return False
    except Exception as e:
        print(f"Error al eliminar el favorito: {e}")
        return False



#CONCLUSION:
#Busca el favorito con Favourite.objects.get(id=fav_id).
#Si existe, lo elimina con favourite.delete().
#Retorna True si la eliminación fue exitosa.