from api.viewsets import  messagesviewsets
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register('message', messagesviewsets)