"""Configuracion de produccion — Semana 12.

Extiende settings.py con valores seguros para despliegue.
Nunca hardcodear secretos: usar variables de entorno.
"""

import os

from .settings import *   # noqa: F401,F403 — importar base

# ── Seguridad ────────────────────────────────────────────────
DEBUG      = os.getenv("DEBUG", "False") == "True"
SECRET_KEY = os.getenv("SECRET_KEY", SECRET_KEY)   # noqa: F405
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS", "localhost,127.0.0.1"
).split(",")

# ── HTTPS (Render provee HTTPS automaticamente) ───────────────
_ssl = os.getenv("SECURE_SSL_REDIRECT", "False") == "True"
SECURE_SSL_REDIRECT   = _ssl
SESSION_COOKIE_SECURE = _ssl
CSRF_COOKIE_SECURE    = _ssl

# ── Archivos estaticos con WhiteNoise ────────────────────────
MIDDLEWARE.insert(                                 # noqa: F405
    MIDDLEWARE.index(                              # noqa: F405
        "django.middleware.security.SecurityMiddleware"
    ) + 1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

STATIC_ROOT         = BASE_DIR / "staticfiles"    # noqa: F405
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)