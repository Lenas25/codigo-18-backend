from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken, AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken,TokenError

# metodo para asignar una token dependiendo del user
def get_tokens_for_user(user):
  token = RefreshToken.for_user(user)
  
  return {
    # refresh sera usado en un futuro para volver a crear un nuevo token cuando el original expire -> un token extra que se puede usar para poder crear un nuevo token con el tiempo de vida
    'refresh': str(token),
    # lo que usaremos hoy sera el access_token
    'access': str(token.access_token)
  }

# function para validar token
def validate_token(token):
  try:
    # UntypedToken -> va a decirnos si el token es valido o no
    # si al tratar de verificar que el token sea valido, este no lo es entonces entrara en un error
    UntypedToken(token)
    return True
  except (InvalidToken, TokenError) as e:
    print(e)
    return False

# payload -> es la informacion que se envia en el body o que se envia como parametro
# reverse engineer, esa funcion obtiene el usuario que contiene el token
def get_payload_from_token(token):
  try:
    return AccessToken(token).payload
  except (InvalidToken, TokenError) as e:
    print(e)
    return False