from django.apps import AppConfig

# Define a new class called PollsConfig that inherits from AppConfig
class PollsConfig(AppConfig):
    # Set the default auto field to be a BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
