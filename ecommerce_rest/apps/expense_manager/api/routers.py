from rest_framework. routers import DefaultRouter
from apps.expense_manager.api.viewsets.expense_viewsets import *

# Declaramos el Router
router = DefaultRouter()

# Registramos las URLS de nuestro router
router.register(r'expense',ExpenseViewSet,basename = 'expense')

# Las asignamos a un urlpatterns para que puedan ser entendidas por Django.
urlpatterns = router.urls