from django.template.library import Library

# Créez une instance de Library
register = Library()

# Importez vos filtres personnalisés
from . import custom_filters

# Enregistrez vos filtres personnalisés
register.filter(custom_filters.custom_filter) # type: ignore

