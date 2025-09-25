# Book Review System Frontend

A Bootstrap 5 frontend implementation of a book review and management system wireframes. This project creates a static HTML/CSS interface that matches the exact wireframe designs for a book review application.

## Project Structure

```
Book_Review_Frontend/
├── index.html              # Welcome page (http://localhost/)
├── books.html              # Books home page (http://localhost/books)
├── add-book.html           # Add book and review page (http://localhost/books/add)
├── book-details.html       # Specific book review page (http://localhost/books/1)
├── user-reviews.html       # User reviews page (http://localhost/users/1)
├── styles.css              # Custom CSS styles
└── README.md               # This file
```

## Pages Overview

### 1. Welcome Page (`index.html`)
- **URL**: `http://localhost/`
- **Features**: 
  - Registration form with name, alias, email, password fields
  - Login form with email and password fields
  - Password validation note (minimum 8 characters)
  - Validation requirements note
- **Bootstrap Components**: Cards, Forms, Alerts

### 2. Books Home Page (`books.html`)
- **URL**: `http://localhost/books`
- **Features**:
  - Welcome message with user name
  - Recent Book Reviews section (latest 3 reviews)
  - Other Books with Reviews section (book title links)
  - Navigation links (Add Book and Review, Logout)
  - Star ratings display
  - User and book title links
- **Bootstrap Components**: Cards, Tables, Buttons, Links

### 3. Add Book and Review Page (`add-book.html`)
- **URL**: `http://localhost/books/add`
- **Features**:
  - Book title input field
  - Author input field
  - Author dropdown selection
  - New author input field
  - Review textarea
  - Rating input (1-5 stars)
  - Navigation links (Home, Logout)
- **Bootstrap Components**: Forms, Select, Textarea, Input Groups

### 4. Specific Book Review Page (`book-details.html`)
- **URL**: `http://localhost/books/1`
- **Features**:
  - Book information display (title and author)
  - Existing reviews with star ratings
  - User name links to user profiles
  - Delete review button for user's own reviews
  - Add new review form
  - Navigation links (Home, Logout)
- **Bootstrap Components**: Cards, Forms, Buttons, Star Ratings

### 5. User Reviews Page (`user-reviews.html`)
- **URL**: `http://localhost/users/1`
- **Features**:
  - User information display (alias, name, email, total reviews)
  - Posted reviews list with book title links
  - Navigation links (Home, Add Book and Review, Logout)
- **Bootstrap Components**: Cards, Lists, Links

## Features Implemented

### ✅ Core Functionality
- User registration and login forms
- Book listing with recent reviews
- Add new book and review functionality
- Individual book review pages
- User profile pages with review history
- Star rating system display
- Navigation between all pages

### ✅ Wireframe Accuracy
- Exact same layout structure as wireframes
- Same form fields and validation messages
- Same navigation flow and user experience
- Same data display format
- Browser-like header simulation
- Proper responsive design

### ✅ Bootstrap 5 Implementation
- Responsive design using Bootstrap 5.3.0
- Cards, forms, buttons, alerts, and tables
- Proper grid system and spacing
- Mobile-friendly responsive design
- Custom styling for enhanced appearance

## Navigation Flow

The application follows the exact navigation flow specified in the wireframes:

1. **Welcome Page** → **Books Home Page** (after login)
2. **Books Home Page** → **Add Book and Review Page** (Add Book and Review button)
3. **Add Book and Review Page** → **Specific Book Review Page** (after adding book)
4. **Books Home Page** → **Specific Book Review Page** (clicking book title)
5. **Specific Book Review Page** → **User Reviews Page** (clicking user name)

## Technologies Used

- **HTML5**: Semantic markup structure
- **Bootstrap 5.3.0**: CSS framework for responsive design
- **Custom CSS**: Additional styling for specific requirements
- **CDN**: Bootstrap loaded from CDN for easy deployment

## Custom Styling

The `styles.css` file includes:
- Browser-like header styling
- Star rating system styling
- Custom card and form styling
- Responsive design adjustments
- Custom spacing and typography
- Link and button hover effects
- Alert box styling with colored borders

## Sample Data

The application includes sample data matching the wireframes:
- **Users**: Jessie, Jerry, Mike, Shirley, David
- **Books**: Divergent, The Greatest Salesman in the World, Tuesdays with Morrie, etc.
- **Reviews**: Sample reviews with star ratings and dates
- **Authors**: Stephen King, Veronica Roth, J.K. Rowling, etc.

## Browser Compatibility

- Modern browsers supporting HTML5 and CSS3
- Bootstrap 5.3.0 compatibility
- Responsive design for mobile and desktop
- Cross-browser compatibility

## Usage

1. Open any HTML file in a web browser
2. Navigate between pages using the provided links
3. All pages are static and don't require a server
4. Forms are for display purposes only (no backend functionality)

## Future Enhancements

This frontend can be easily integrated with:
- Django backend for full functionality
- JavaScript for form validation and interactivity
- AJAX for dynamic content loading
- Database integration for real data
- User authentication system
- Review management system

## Wireframe Compliance

This implementation follows the exact wireframe specifications:
- Same layout structure and positioning
- Same form fields and validation messages
- Same navigation flow and user experience
- Same data display format and styling
- Same responsive behavior
- Browser-like header simulation
- Proper color scheme and typography
