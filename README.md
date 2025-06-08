# JournalingApp

#### Video Demo:  <URL HERE>

## Description

JournalingApp is a full-stack web application designed to help users relieve the tensions and anxieties of daily life through private, secure, and visually appealing digital journaling. It combines a Django REST API backend with a modern React frontend, enabling users to register, authenticate, and manage their journal entries effortlessly. With a focus on privacy, intuitive UX, and extensibility, JournalingApp is ideal both for personal journaling and as a foundation for advanced note-taking platforms.

## Project Overview

The core idea behind JournalingApp is to offer a seamless journaling platform where users can create, edit, and delete their notes, while also managing their personal profile and social links. The backend ensures robust authentication and data integrity, while the frontend focuses on a delightful user experience with responsive layouts and interactive features. The project is structured to encourage maintainability and future enhancements, such as AI-powered suggestions or analytics.

## Backend Structure (Django)

The backend is implemented using Django and Django REST Framework, providing a secure API for all journal and user operations. Key files and their roles include:

- `manage.py`: Standard Django entry point for administrative tasks.
- `backend/settings.py`: Configures installed apps (including `rest_framework`, `corsheaders`, and `journal_app`), database (SQLite3), authentication (JWT), and CORS for frontend-backend communication.
- `backend/urls.py`: Routes API endpoints, including registration, profile, and JWT authentication.
- `journal_app/models.py`: Defines two main models:
  - `Note`: Represents a journal entry, linked to a user, with title, content, and timestamp.
  - `UserProfile`: Extends the default user with first/last name and social links (GitHub, Twitter, Instagram).
- `journal_app/serializers.py`: Handles serialization for API input/output, including custom logic for user registration and profile creation.
- `journal_app/views.py`: Implements API endpoints using Django REST Framework viewsets and generics. Notable endpoints include:
  - `NoteViewSet`: CRUD operations for notes, restricted to the authenticated user.
  - `UserProfileViewSet` and `UserProfileView`: Profile management and retrieval.
  - `RegisterView`: Custom registration logic, creating both user and profile.
- `journal_app/permissions.py`: Custom permission (`IsOwner`) to ensure users can only access their own notes.
- `journal_app/urls.py`: Registers API routes for notes and user profiles.
- `journal_app/migrations/`: Contains migration files for database schema evolution.

### Design Decisions (Backend)

- **JWT Authentication**: Chosen for stateless, secure API access, enabling easy integration with modern frontends.
- **Custom UserProfile**: Instead of extending the default user model, a separate `UserProfile` model is linked via a one-to-one relationship, allowing for flexible profile fields without interfering with Django's auth system.
- **Permissions**: The `IsOwner` permission class enforces strict data privacy, ensuring users cannot access or modify others' notes.
- **CORS**: Enabled via `corsheaders` to allow local frontend development and future deployment flexibility.

## Frontend Structure (React)

The frontend is built with React, using functional components, React Router for navigation, and Axios for API communication. The UI is styled with custom CSS for a modern, inviting look. Key files and their purposes include:

- `src/App.js`: Main entry point, sets up routes for landing, main menu, journals, and profile pages. Uses `ProtectedRoute` to guard authenticated routes.
- `src/pages/LandingPage.js`: Welcomes users, provides login and registration options, and features animated SVG backgrounds for visual appeal.
- `src/pages/MainMenuPage.js`: Displays the user's profile and social links, with navigation to journals and a logout button.
- `src/pages/JournalsPage.js`: Core journaling interface, allowing users to create, view, edit, delete, and download notes. Features modal editing and responsive design.
- `src/pages/ProfilePage.js`: Registration form for new users, collecting username, password, and profile details.
- `src/components/LogoutButton.js`: Handles user logout, clearing tokens and redirecting to the landing page.
- `src/routes/ProtectedRoute.js`: Ensures only authenticated users can access certain routes, checking JWT validity.
- `src/utils/auth.js`: Utility for extracting user ID from JWT tokens.
- `src/styles/`: Contains CSS files for each major component/page, supporting a consistent and attractive UI.
- `public/data/` and `public/menu-icon/`: SVG assets for backgrounds and icons, enhancing the user experience.

### Design Decisions (Frontend)

- **Component Structure**: Pages are separated by function (landing, main menu, journals, profile) for clarity and scalability.
- **Protected Routes**: Implemented to prevent unauthorized access to user data, improving security and user experience.
- **SVG Animations**: Chosen to create a welcoming, personalized feel, making journaling more enjoyable.
- **Axios for API Calls**: Preferred for its simplicity and widespread use in React projects.
- **Download as DOCX**: Users can export notes, increasing data portability and user trust.

## File-by-File Breakdown

- **Backend**:
  - `models.py`: Data models for notes and user profiles.
  - `serializers.py`: Data validation and transformation for API endpoints.
  - `views.py`: Business logic for note and user operations.
  - `permissions.py`: Custom access control.
  - `urls.py`: API route definitions.
  - `migrations/`: Database schema history.
- **Frontend**:
  - `App.js`: Routing and app structure.
  - `pages/`: UI for each major user flow.
  - `components/`: Reusable UI elements (e.g., logout button).
  - `routes/`: Route protection logic.
  - `utils/`: Helper functions for authentication.
  - `styles/`: CSS for a polished look.
  - `public/`: Static assets (SVGs, icons, manifest).

## Reflections and Future Directions

During development, several design choices were debated. For example, whether to extend the Django user model directly or use a separate profile model; the latter was chosen for flexibility and to avoid migration issues. JWT was selected over session authentication for its compatibility with SPAs. The frontend's use of custom CSS and SVGs was preferred over a UI framework to allow for a unique, personal aesthetic.

Future improvements could include AI-powered journaling suggestions, richer text editing, and analytics on journaling habits. The current structure is designed to support such enhancements with minimal refactoring.

## Conclusion

JournalingApp offers a secure, aesthetically pleasing, and extensible digital journaling experience. Its thoughtful design, clean code organization, and user privacy focus make it suitable for both personal use and further development. Contributions and feedback are always welcome!