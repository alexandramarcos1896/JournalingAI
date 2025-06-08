from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from .models import Note
from .serializers import NoteSerializer
# from .serializers import RegisterSerializer
from .serializers import UserProfile
from .models import UserProfile
from .serializers import UserSerializer

from .serializers import UserProfileSerializer
from rest_framework import permissions
from .permissions import IsOwner 

# from django.contrib.auth.hashers import make_password

# class NoteViewSet(viewsets.ModelViewSet):
#     queryset = Note.objects.all().order_by('-created_at')
#     serializer_class = NoteSerializer

#     def update(self, request, *args, **kwargs):
#         partial = True  # <- allow partial updates
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    # queryset = Note.objects.none()  # Dummy queryset just to satisfy the router

    def get_queryset(self):
        # Only return notes that belong to the authenticated user
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the note to the authenticated user
        serializer.save(user=self.request.user)
    
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

@csrf_exempt
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=401)

# @csrf_exempt
# @api_view(['GET'])
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()  # make a mutable copy
        profile_data = data.pop('profile', {})
        print(profile_data)  # Debugging line to check profile data
        try:
            # Create the user
            user = User.objects.create_user(
                username=request.data['username'],
                password=request.data['password'],
                first_name=profile_data.get('first_name', ''),
                last_name=profile_data.get('last_name', '')
            )

            # Create profile
            UserProfile.objects.create(
                user = user,
                # username=request.data['username'],
                first_name=profile_data.get('first_name', ''),
                last_name=profile_data.get('last_name', ''),
                github=profile_data.get('github', ''),
                twitter=profile_data.get('twitter', ''),
                instagram=profile_data.get('instagram', '')
            )
            print(f"User {user.username} created with profile: {profile_data}")  # Debugging line
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = request.user.profile
        return Response({
            "name": profile.first_name,
            "last_name": profile.last_name,
            "github": profile.github,
            "twitter": profile.twitter,
            "instagram": profile.instagram
        })
        
