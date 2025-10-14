## 📚 **Project Title: Library Management System (LMS)**

### 🧠 **Overview**

The **Library Management System (LMS)** is a Django-based web application designed to manage books within a digital library.
It allows the **Admin** user to add books with detailed information such as title, author, price, number of pages, status, category, rating, and description — as well as upload book cover images.
The system focuses on CRUD (Create, Read, Update, Delete) operations through Django’s admin panel and a simple, responsive HTML/CSS interface.

---

### 🧰 **Tech Stack**

| Component           | Details                                             |
| ------------------- | --------------------------------------------------- |
| **Backend**         | Django 5.x (Python)                                 |
| **Frontend**        | HTML, CSS (custom responsive design, no frameworks) |
| **Database**        | SQLite (default Django database)                    |
| **Authentication**  | Django built-in user system (Admin only)            |
| **Version Control** | Git + GitHub                                        |

---

### 🧩 **Core Features**

| Requirement                                | How It’s Implemented                                                                   |
| ------------------------------------------ | -------------------------------------------------------------------------------------- |
| **Single Django app with a clear purpose** | The `lms_app` manages books and categories.                                            |
| **CRUD functionality**                     | Admin can Create, Read, Update, and Delete both books and categories.                  |
| **Admin panel for management**             | The Django Admin interface is customized to manage books with images and details.      |
| **Dynamic data rendering**                 | Books are displayed dynamically using Django Template Language (DTL).                  |
| **Consistent & responsive styling**        | All pages are styled with custom HTML and CSS to ensure a clean and responsive design. |

---

### 🧱 Data Model (ERD) - Vertical Layout

+----------------+
| User/Admin |
+----------------+
| username |
| password |
+----------------+
|
| 1
|
v
+----------------+
| Category |
+----------------+
| name |
+----------------+
|
| 1
|
v
+------------------------------+
| Book |
+------------------------------+
| title |
| author |
| photo_book |
| pages |
| price |
| rental_price_day |
| status (Available/Rental/Sold)|
| category (FK to Category) |
| rating |
| description |
+------------------------------+

**🔗 Relationships:**

* Each **Category** can have many **Books**.
* Each **Book** belongs to one **Category**.
* Only one **Admin User** can create many Books.
* Only one **Admin User** can create many Categories.
* Only one **Admin User** manages all entities.


---

### 🧭 **User Stories**

* As an **Admin**, I can log in to the admin dashboard.
* As an **Admin**, I can add new books with full details.
* As an **Admin**, I can add new category.
* As an **Admin**, I can view all books stored in the system.
* As an **Admin**, I can edit or delete any book or category.
* As a **Visitor**, I can browse all books displayed on the public homepage.

---

### 💻 **Pages (HTML Templates)**

| Page                            | Description                                                                                        |
| ------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Home (All Books)**            | Displays all books with cover image, title, and author.                                            |
| **Book Detail**                 | Shows complete information about a selected book (title, author, price, description, image, etc.). |
| **Add / Edit Book (Admin)**     | Forms to add or update book information.                                                           |
| **Category Management (Admin)** | Admin page to manage and create categories.                                                        |
| **Login / Logout**              | Authentication pages for admin login and logout.                                                   |

---

### ⚙️ **Core Views / CRUD**

| View           | Description                               |
| -------------- | ----------------------------------------- |
| **ListView**   | Displays all books on the homepage (`/`). |
| **CreateView** | Allows adding a new book.                 |
| **UpdateView** | Allows editing book details.              |
| **DeleteView** | Allows deleting a book.                   |
| **DetailView** | Displays details of a single book.        |

---

### 🗓️ **4-Day Development Plan**

| Day                                | Focus                                                                                  | Tasks |
| ---------------------------------- | -------------------------------------------------------------------------------------- | ----- |
| **Day 1 – Setup & Models**         | Project setup, create models (Book & Category), configure media folder, test in admin. |       |
| **Day 2 – Admin Panel + CRUD**     | Implement CRUD for Book and Category, secure access to admin only.                     |       |
| **Day 3 – Templates & Display**    | Create templates for homepage and book details, connect to views.                      |       |
| **Day 4 – CSS + README + Testing** | Add responsive CSS, finalize README, and test the project.                             |       |

---

### 🧮 **Example Query Logic**

Display all books:

```python
books = Book.objects.all().order_by('title')
```

Filter books by category:

```python
books = Book.objects.filter(category__name='Science')
```

Display only available books:

```python
books = Book.objects.filter(status='available')
```

---

### 🌟 **Stretch Goals (Optional Enhancements)**

* Add a **book rental system** with time tracking.
* Add a **search bar** (by title or author).
* Include a **rating system** for books.
* Add **pagination** for large collections.
* Add **role-based permissions** (sub-admins).
* Implement a **visual dashboard** with statistics.

---

### 🧾 **Challenges & Solutions**

| Challenge                           | Solution                                                             |
| ----------------------------------- | -------------------------------------------------------------------- |
| Handling image uploads              | Configured `MEDIA_URL` and `MEDIA_ROOT` in settings.py.              |
| Defining book-category relationship | Used `ForeignKey` with `on_delete=models.PROTECT`.                   |
| Customizing admin interface         | Changed admin site title to *Library Management System Admin Panel*. |
| Displaying book images in admin     | Used `list_display` and media configuration to show images properly. |

---

### 🧠 **Future Improvements**

* Build a **modern frontend** using React or Vue.js instead of relying only on Django Admin.
* Add **user registration and login** for normal users (not just admin).
* Implement a **real book borrowing system** with deadlines and late fees.
* Create an **Analytics Dashboard** showing statistics by category or status.
* Allow **PDF file uploads** in addition to book images.
* Add an **Author model** to link multiple books to one author.



