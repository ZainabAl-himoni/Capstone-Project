## 📚 **Project Title: NestBook **

### 🧠 **Overview**

The **NestBook** :books: Project Title: NestBook – Library Management System App
:brain: Overview
NestBook is a web application that allows users to create and manage their personal book collections.
 Each user can log in, add books with titles, authors, descriptions, and prices, and upload cover images to visualize their library.
 The app focuses on CRUD functionality, authentication, and a clean, responsive HTML/CSS interface.

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

![ERD](pic/ERD.png)


**🔗 Relationships:**

* Each **Category** can have many **Books**.
* Each **Book** belongs to one **Category**.
* Only one **User** can create many Books.
* Only one **User** can create many Categories.
* Only one **User** manages all entities.


---

### 🧭 **User Stories**

- As a **user**, I can register and log in to my account.  
- As a **user**, I can add new categories to organize my books.  
- As a **user**, I can add new books with details such as **title**, **author**, **description**, **price**, **image**, **pages**, **rental price**, and **status**.  
- As a **user**, I can assign a book to a specific category.  
- As a **user**, I can view all books  
- As a **user**, I can edit or delete my own books.  
- As a **user**, I can edit or delete categories that I created.  
- As a **user**, I can add, edit, and delete comments on books.  

- As a **visitor**, I can view all books displayed on the public homepage.  
- As a **visitor**, I can add, edit, and delete my own comments on books.  
- As a **visitor**, I cannot add, edit, or delete books or categories.  


---

### 💻 **Pages (HTML Templates)**

| Page                            | Description                                                                                        |
| ------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Home (All Books)**            | Displays all books with cover image, title, and author.                                            |
| **Book Detail**                 | Shows complete information about a selected book (title, author, price, description, image, etc.). |
| **Add / Edit Book**     | Forms to add or update book information.                                                           |
| **Category Management** | Admin page to manage and create categories.                                                        |
| **Login / Logout**              | Authentication pages for admin login and logout.                                                   |

---

### ⚙️ **Core Views / CRUD**

| View           | Description                               |
| -------------- | ----------------------------------------- |
| **ListView**   | Displays all books on the homepage (`/`). |
| **CreateView** | Allows adding a new book and category.    |
| **UpdateView** | Allows editing book details and category. |
| **DeleteView** | Allows deleting a book and category.      |
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
| Displaying book images in admin     | Used `list_display` and media configuration to show images properly. |

---

### 🧠 **Future Improvements**

* Build a **modern frontend** using React or Vue.js instead of relying only on Django Admin.
* Add **user registration and login** for normal users (not just admin).
* Implement a **real book borrowing system** with deadlines and late fees.
* Create an **Analytics Dashboard** showing statistics by category or status.
* Allow **PDF file uploads** in addition to book images.
* Add an **Author model** to link multiple books to one author.



