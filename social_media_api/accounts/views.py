from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username = serializer.validated_data['username'],
                password = serializer.validated_data['password']
            )
            if user:
                if Token.objects.filter(user=user).exists():
                    token = Token.objects.get(user=user)
                else:
                    token = Token.objects.create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
class ProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serialzier = UserSerializer(user)
        return Response(serialzier.data, status=status.HTTP_200_OK)

class FollowUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = get_user_model().objects.get(id=user_id)
            if user_to_follow == request.user:
                return Response({"detail": "cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
            request.user.following.add(user_to_follow)
            return Response({"detail": f"following {user_to_follow.username}"}, status=status.HTTP_200_OK)
        except get_user_model().DoesNotExist:
            return Response({"detail": "user not found"}, status=status.HTTP_404_NOT_FOUND)


class UnfollowUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = get_user_model().objects.get(id=user_id)
            if user_to_unfollow == request.user:
                return Response({"detail": "cannot unfollow self"}, status=status.HTTP_400_BAD_REQUEST)
            request.user.following.remove(user_to_unfollow)
            return Response({"detail": f"Unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
        except get_user_model.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        