class Config:
    CELERY_BROKER = "redis://redis:6379/0"
    CELERY_BACKEND = "redis://redis:6379/0"
