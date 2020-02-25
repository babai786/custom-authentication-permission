from rest_framework.permissions import  BasePermission,SAFE_METHODS


#ONLY SAFE METHODS


class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return  False


#ONLY GET OR PATCH

class OnlyGETOrPatch(BasePermission):
    def has_permission(self, request, view):
        allowed_permission=['GET','PATCH']
        if request.method in allowed_permission:
            return True
        else:
            return False

## if name is sunny return true


class Custom(BasePermission):
    def has_permission(self, request, view):
        username=request.user.username
        if username.lower()=='tubai':
            return True
        elif username!='' and len(username)>2 and request.method in SAFE_METHODS:
            return True
        else:
            return False
