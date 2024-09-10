from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from .serializers import GroupSerializer, UserSerializer
from core.models import Entidad
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method="post",
    operation_description="Login con email y password. Devuelve un token de autenticación si las credenciales son correctas.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Correo electrónico del usuario'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Contraseña del usuario'),
        },
        required=['email', 'password'],
    ),
    responses={
        200: openapi.Response(
            description="Respuesta exitosa con token y datos del usuario",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "user": openapi.Schema(type=openapi.TYPE_OBJECT, description="Datos del usuario"),
                    "groups": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT), description="Grupos del usuario"),
                    "token": openapi.Schema(type=openapi.TYPE_STRING, description="Token de autenticación"),
                    "permissions": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING), description="Permisos del usuario"),
                    "entidad_documento": openapi.Schema(type=openapi.TYPE_STRING, description="Número de documento de la entidad"),
                    "entidad_razon_ocial": openapi.Schema(type=openapi.TYPE_STRING, description="Razón social de la entidad"),
                    "entidad_nombre_comercial": openapi.Schema(type=openapi.TYPE_STRING, description="Nombre comercial de la entidad"),
                },
            )
        ),
        400: "Bad Request (falta email o password)",
        401: "Unauthorized (credenciales incorrectas o usuario no pertenece al grupo 'usuario')"
    },
)
@api_view(["POST"])
def login(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=email, is_active=True)
            print(email)
        except:
            return Response(
                "El usuario   no existe",
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if user.check_password(password):
            token, _ = Token.objects.get_or_create(user=user)
            user_model = User.objects.get(email=email)
            groups = user_model.groups.all()
            if not groups.filter(name="usuario").exists():
                return Response(
                    "El usuario con este correo electrónico no existe",
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            permissions = user_model.get_user_permissions()
            entidad = Entidad.objects.get(user=user_model)
            return Response(
                {
                    "user": UserSerializer(user_model).data,
                    "groups": GroupSerializer(groups, many=True).data,
                    "token": token.key,
                    "permissions": permissions,
                    "entidad_documento": entidad.numeroDocumento,
                    "entidad_razon_ocial": entidad.razonSocial,
                    "entidad_nombre_comercial": entidad.nombreComercial,
                }
            )
        else:
            return Response(
                "Wrong email or password",
                status=status.HTTP_401_UNAUTHORIZED,
            )


@swagger_auto_schema(
    method="post",
    operation_description="Obtener datos del usuario autenticado utilizando el token.",
    responses={
        200: openapi.Response(
            description="Datos del usuario autenticado",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "user": openapi.Schema(type=openapi.TYPE_OBJECT, description="Datos del usuario"),
                    "groups": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT), description="Grupos del usuario"),
                    "token": openapi.Schema(type=openapi.TYPE_STRING, description="Token de autenticación"),
                    "permissions": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING), description="Permisos del usuario"),
                    "persona_numero_documento": openapi.Schema(type=openapi.TYPE_STRING, description="Número de documento de la entidad asociada"),
                },
            )
        ),
        401: "Unauthorized (usuario no pertenece al grupo 'usuario')"
    },
)
@api_view(["POST"])
def get_user_data_by_token(request):
    if request.method == "POST":
        user = request.user

        token, created = Token.objects.get_or_create(user=user)
        user_model = User.objects.get(email=user.email)
        groups = user_model.groups.all()

        if not groups.filter(name="usuario").exists():
            return Response(
                "El usuario con este correo electrónico no existe",
                status=status.HTTP_401_UNAUTHORIZED,
            )
        permissions = user_model.get_user_permissions()
        entidad = Entidad.objects.get(user=user_model)
        return Response(
            {
                "user": UserSerializer(user_model).data,
                "groups": GroupSerializer(groups, many=True).data,
                "token": token.key,
                "permissions": permissions,
                "persona_numero_documento": entidad.numeroDocumento,
            }
        )
    

@swagger_auto_schema(
    method="post",
    operation_description="Registro de un nuevo usuario. Devuelve los datos del usuario y su token.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Correo electrónico del usuario'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Contraseña del usuario'),
            'nombre_comercial': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre comercial de la entidad'),
            'razon_social': openapi.Schema(type=openapi.TYPE_STRING, description='Razón social de la entidad'),
            'numero_documento': openapi.Schema(type=openapi.TYPE_STRING, description='Número de documento de la entidad'),
        },
        required=['email', 'password', 'nombre_comercial', 'razon_social', 'numero_documento'],
    ),
    responses={
        201: openapi.Response(
            description="Usuario creado correctamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "user": openapi.Schema(type=openapi.TYPE_OBJECT, description="Datos del usuario"),
                    "token": openapi.Schema(type=openapi.TYPE_STRING, description="Token de autenticación"),
                    "entidad_documento": openapi.Schema(type=openapi.TYPE_STRING, description="Número de documento de la entidad"),
                    "entidad_razon_ocial": openapi.Schema(type=openapi.TYPE_STRING, description="Razón social de la entidad"),
                    "entidad_nombre_comercial": openapi.Schema(type=openapi.TYPE_STRING, description="Nombre comercial de la entidad"),
                },
            )
        ),
        400: "Bad Request (falta algún campo requerido o el usuario ya está registrado)",
    },
)
@api_view(["POST"])
def register(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")
        nombre_comercial = request.data.get("nombre_comercial", "")
        razon_social = request.data.get("razon_social", "")
        numero_documento = request.data.get("numero_documento", "")

        # Check if all required fields are present
        if not email or not password or not nombre_comercial or not razon_social or not numero_documento:
            return Response(
                {"error": "Faltan campos requeridos"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if user already exists
        if User.objects.filter(username=email).exists():
            return Response(
                {"error": "Este usuario ya está registrado"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create the new user
        user = User.objects.create_user(username=email, email=email, password=password)

        # Assign the user to the "usuario" group (if needed)
        usuario_group, created = Group.objects.get_or_create(name="usuario")
        user.groups.add(usuario_group)

        # Create the associated Entidad (business entity) for the user
        entidad = Entidad.objects.create(
            user=user,
            nombreComercial=nombre_comercial,
            razonSocial=razon_social,
            numeroDocumento=numero_documento
        )

        # Create the token for authentication
        token, _ = Token.objects.get_or_create(user=user)

        # Return a response with user and entity information
        return Response(
            {
                "user": UserSerializer(user).data,
                "token": token.key,
                "entidad_documento": entidad.numeroDocumento,
                "entidad_razon_ocial": entidad.razonSocial,
                "entidad_nombre_comercial": entidad.nombreComercial,
            },
            status=status.HTTP_201_CREATED
        )
