from django.contrib.auth.models import BaseUserManager

# para manejar la creacion de usuarios por la terminal
class UsuarioManager(BaseUserManager):
  def create_superuser(self, correo, nombre, apellido, password):
    if not correo:
      raise ValueError('El usuario debe tener un correo')
    
    correo_normalizado = self.normalize_email(correo)
    nuevo_usuario = self.model(correo = correo_normalizado, nombre=nombre, apellido=apellido)
    # metodo propio del auth user que genera el hash
    nuevo_usuario.set_password(password)
    nuevo_usuario.is_superuser=True
    nuevo_usuario.is_staff=True
    
    nuevo_usuario.save()