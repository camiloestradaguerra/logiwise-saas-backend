from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

# Configuración básica (en producción, usa variables de entorno seguras)
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

from passlib.hash import sha256_crypt

# Simulación de base de datos de usuarios
fake_users_db = {
    "admin@example.com": {
        "username": "admin@example.com",
        "full_name": "Admin User",
        # Contraseña: "admin" (sha256_crypt)
        "hashed_password": "$5$rounds=535000$QwErTyUiOp$QwErTyUiOpQwErTyUiOpQwErTyUiOpQwErTyUiOpQwErTyUiOpQwErTyUiOpQwErTyUiOpQwErTyUiOpQwErTyUiOpQwErTyUiOp/",  # "admin"
        "role": "admin",
        "disabled": False,
    },
}

# Usar sha256_crypt para compatibilidad multiplataforma
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

router = APIRouter()

# Modelos de usuario (puedes usar Pydantic para más detalle)
class User:
    def __init__(self, username, full_name, role, disabled):
        self.username = username
        self.full_name = full_name
        self.role = role
        self.disabled = disabled

class UserInDB(User):
    def __init__(self, username, full_name, role, disabled, hashed_password):
        super().__init__(username, full_name, role, disabled)
        self.hashed_password = hashed_password

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/auth/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}

# Dependencia para proteger endpoints
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if username is None or role is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username)
    if user is None:
        raise credentials_exception
    return user

# Ejemplo de endpoint protegido por rol
@router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "role": current_user.role}

# Para proteger endpoints por rol:
def require_role(required_role: str):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(status_code=403, detail="No tienes permisos para acceder a este recurso.")
        return current_user
    return role_checker

# Ejemplo de endpoint solo para admin
@router.get("/admin/only")
async def admin_only(current_user: User = Depends(require_role("admin"))):
    return {"msg": "Solo admin puede ver esto."}
