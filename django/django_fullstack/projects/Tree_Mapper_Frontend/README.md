# Tree Mapper Frontend

A Bootstrap 5 frontend implementation of the Tree Mapper wireframes. This project creates a static HTML/CSS interface that matches the exact wireframe designs for a tree mapping application.

## Project Structure

```
Tree_Mapper_Frontend/
├── index.html              # Login/Register page (localhost:5000)
├── dashboard.html          # Dashboard page (localhost:5000/dashboard)
├── edit-tree.html          # Edit tree details page (localhost:5000/trees/edit/1)
├── add-tree.html           # Add new tree page (localhost:5000/trees/new)
├── tree-details.html       # Tree details page (localhost:5000/trees/4)
├── trees-by-zip.html       # Trees by zip code page (localhost:5000/trees/zip/96789)
├── styles.css              # Custom CSS styles
└── README.md               # This file
```

## Pages Overview

### 1. Login/Register Page (`index.html`)
- **URL**: `localhost:5000`
- **Features**: 
  - Registration form with validation requirements
  - Login form with authentication requirements
  - MVP validation boxes showing requirements
- **Bootstrap Components**: Cards, Forms, Alerts

### 2. Dashboard Page (`dashboard.html`)
- **URL**: `localhost:5000/dashboard`
- **Features**:
  - Welcome message with logout link
  - Table of all mapped trees
  - Edit/Delete links for user's own trees
  - "Post a new tree" button
  - Zip code badges (stretch goal feature)
- **Bootstrap Components**: Tables, Cards, Buttons, Badges

### 3. Edit Tree Page (`edit-tree.html`)
- **URL**: `localhost:5000/trees/edit/1`
- **Features**:
  - Pre-populated form fields
  - Error message display
  - Navigation links
  - MVP and stretch goal requirements
- **Bootstrap Components**: Forms, Alerts, Input Groups

### 4. Add Tree Page (`add-tree.html`)
- **URL**: `localhost:5000/trees/new`
- **Features**:
  - New tree form with validation
  - Error message display
  - Pre-filled example data
  - MVP and stretch goal validation requirements
- **Bootstrap Components**: Forms, Alerts, Input Groups

### 5. Tree Details Page (`tree-details.html`)
- **URL**: `localhost:5000/trees/4`
- **Features**:
  - Tree information display
  - Visitor list (stretch goal)
  - "Did you visit this tree?" link
  - MVP and stretch goal requirements
- **Bootstrap Components**: Cards, Alerts

### 6. Trees by Zip Code Page (`trees-by-zip.html`)
- **URL**: `localhost:5000/trees/zip/96789`
- **Features**:
  - Stretch goal page indicator
  - Table of trees in specific zip code
  - Stretch goal requirements
- **Bootstrap Components**: Tables, Cards, Alerts

## Features Implemented

### MVP Features (Yellow Boxes)
- ✅ All form validations as specified
- ✅ User authentication requirements
- ✅ Tree listing with edit/delete functionality
- ✅ Pre-populated form fields
- ✅ Error message display
- ✅ Navigation between pages

### Stretch Goals (Purple Boxes)
- ✅ Zip code field and display
- ✅ Zip code badges in dashboard
- ✅ Trees by zip code page
- ✅ Visitor tracking system
- ✅ Additional validation requirements

## Technologies Used

- **HTML5**: Semantic markup structure
- **Bootstrap 5.3.0**: CSS framework for responsive design
- **Custom CSS**: Additional styling for specific requirements
- **CDN**: Bootstrap loaded from CDN for easy deployment

## Browser Compatibility

- Modern browsers supporting HTML5 and CSS3
- Bootstrap 5.3.0 compatibility
- Responsive design for mobile and desktop

## Usage

1. Open any HTML file in a web browser
2. Navigate between pages using the provided links
3. All pages are static and don't require a server
4. Forms are for display purposes only (no backend functionality)

## Custom Styling

The `styles.css` file includes:
- Purple badge styling for zip codes
- Custom button and form styling
- Responsive design adjustments
- Alert box styling with colored borders
- Custom spacing and typography

## Wireframe Compliance

This implementation follows the exact wireframe specifications:
- Same layout structure
- Same color scheme (green for Tree Mapper branding)
- Same form fields and validation messages
- Same table structure and data
- Same navigation and user flow
- MVP and stretch goal indicators as specified

## Future Enhancements

This frontend can be easily integrated with:
- Django backend for full functionality
- JavaScript for form validation
- AJAX for dynamic content loading
- Database integration for real data
