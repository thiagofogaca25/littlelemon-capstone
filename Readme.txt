Little Lemon Capstone Project

API endpoints to test:

Authentication:
- POST /api/token/            → get JWT token
- POST /api/token/refresh/    → refresh JWT token

Menu:
- GET /api/menu/              → list all menu items
- POST /api/menu/             → create menu item
- GET /api/menu/<id>/         → retrieve menu item
- PUT /api/menu/<id>/         → update menu item
- DELETE /api/menu/<id>/      → delete menu item

Booking:
- GET /api/booking/           → list all bookings
- POST /api/booking/          → create booking
- GET /api/booking/<id>/      → retrieve booking
- PUT /api/booking/<id>/      → update booking
- DELETE /api/booking/<id>/   → delete booking
