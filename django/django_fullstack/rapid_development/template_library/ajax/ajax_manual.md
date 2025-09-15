# 🚀 AJAX Quick Reference Manual

## Overview
This manual provides quick AJAX patterns for common Django scenarios. Copy, paste, and customize as needed.

## 🔧 Basic AJAX Setup

### 1. CSRF Token Function
```javascript
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
```

### 2. Basic AJAX Form Submission
```javascript
const form = document.getElementById('my-form');
const submitBtn = document.getElementById('submit-btn');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(form);
    const csrftoken = getCookie('csrftoken');
    
    submitBtn.disabled = true;
    
    try {
        const response = await fetch('/ajax-endpoint/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            body: formData
        });
        
        if (response.ok) {
            const data = await response.json();
            // Handle success
            showSuccessMessage(data.message);
        } else {
            const data = await response.json();
            // Handle errors
            showErrors(data.errors);
        }
    } catch (error) {
        console.error('Error:', error);
        showErrorMessage('An error occurred');
    } finally {
        submitBtn.disabled = false;
    }
});
```

## 📝 Common AJAX Patterns

### 1. Form Validation
```javascript
// Real-time validation
document.getElementById('email').addEventListener('blur', async (e) => {
    const email = e.target.value;
    if (email) {
        const response = await fetch('/check-email/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({email: email})
        });
        
        const data = await response.json();
        if (data.valid) {
            e.target.classList.remove('is-invalid');
            e.target.classList.add('is-valid');
        } else {
            e.target.classList.remove('is-valid');
            e.target.classList.add('is-invalid');
            document.getElementById('email-error').textContent = data.message;
        }
    }
});
```

### 2. Delete with Confirmation
```javascript
function deleteItem(id) {
    if (confirm('Are you sure you want to delete this item?')) {
        fetch(`/delete-item/${id}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Remove item from DOM
                document.getElementById(`item-${id}`).remove();
                showSuccessMessage('Item deleted successfully');
            } else {
                showErrorMessage(data.message);
            }
        });
    }
}
```

### 3. Dynamic Content Loading
```javascript
function loadMoreItems(page) {
    fetch(`/load-items/?page=${page}`)
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('items-container');
            data.items.forEach(item => {
                container.innerHTML += createItemHTML(item);
            });
        });
}
```

### 4. Search with Debouncing
```javascript
let searchTimeout;
document.getElementById('search').addEventListener('input', (e) => {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
        performSearch(e.target.value);
    }, 300);
});

function performSearch(query) {
    fetch(`/search/?q=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            updateSearchResults(data.results);
        });
}
```

## 🎯 Django View Patterns

### 1. AJAX Form Processing
```python
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

@require_POST
def ajax_create_item(request):
    try:
        # Process form data
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        # Create item
        item = Item.objects.create(
            name=name,
            description=description,
            user=request.user
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Item created successfully',
            'item_id': item.id
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)
```

### 2. AJAX Validation
```python
@require_POST
def check_email(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({
                'valid': False,
                'message': 'Email already exists'
            })
        else:
            return JsonResponse({
                'valid': True,
                'message': 'Email is available'
            })
            
    except Exception as e:
        return JsonResponse({
            'valid': False,
            'message': 'Invalid request'
        })
```

### 3. AJAX Delete
```python
@require_POST
def ajax_delete_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id, user=request.user)
        item.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Item deleted successfully'
        })
        
    except Item.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Item not found'
        }, status=404)
```

## 🎨 UI Feedback Patterns

### 1. Success Message
```javascript
function showSuccessMessage(message) {
    const container = document.getElementById('messages');
    container.innerHTML = `
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
}
```

### 2. Error Display
```javascript
function showErrors(errors) {
    // Clear previous errors
    document.querySelectorAll('.is-invalid').forEach(el => {
        el.classList.remove('is-invalid');
    });
    document.querySelectorAll('.invalid-feedback').forEach(el => {
        el.textContent = '';
    });
    
    // Show new errors
    for (const [field, messages] of Object.entries(errors)) {
        const input = document.getElementsByName(field)[0];
        const errorDiv = document.getElementById(`error-${field}`);
        
        if (input) input.classList.add('is-invalid');
        if (errorDiv) errorDiv.textContent = messages.join(', ');
    }
}
```

### 3. Loading States
```javascript
function setLoadingState(button, isLoading) {
    if (isLoading) {
        button.disabled = true;
        button.innerHTML = '<span class="spinner-border spinner-border-sm" role="status"></span> Loading...';
    } else {
        button.disabled = false;
        button.innerHTML = 'Submit';
    }
}
```

## 🔗 URL Patterns
```python
# urls.py
urlpatterns = [
    path('ajax/create-item/', views.ajax_create_item, name='ajax_create_item'),
    path('ajax/check-email/', views.check_email, name='check_email'),
    path('ajax/delete-item/<int:item_id>/', views.ajax_delete_item, name='ajax_delete_item'),
    path('ajax/search/', views.ajax_search, name='ajax_search'),
]
```

## 🚨 Common Issues & Solutions

### 1. CSRF Token Issues
- Always include CSRF token in headers
- Use `getCookie('csrftoken')` function
- Ensure Django view accepts POST requests

### 2. JSON Response Issues
- Use `JsonResponse` in Django views
- Handle both success and error cases
- Return appropriate HTTP status codes

### 3. Form Data Issues
- Use `FormData` for file uploads
- Use `JSON.stringify()` for JSON data
- Set correct Content-Type headers

### 4. Error Handling
- Always wrap AJAX calls in try-catch
- Provide user feedback for all scenarios
- Handle network errors gracefully
