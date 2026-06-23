# 🎓 CollegeListSearch

A modern Full Stack College Discovery Platform that helps students search, compare, and explore colleges based on location, fees, ratings, and other important information. The platform also includes a college predictor tool to recommend colleges based on entrance exam rank.

## 🚀 Features

### 🔍 College Search & Filtering
- Search colleges by name
- Filter by:
  - Location
  - Fees
  - Rating
  - College Type
- Pagination for better performance

### 🏫 College Details
- College overview
- Available courses
- Placement statistics
- Student reviews
- Fee structure

### ⚖️ Compare Colleges
Compare up to 3 colleges side by side based on:
- Fees
- Rating
- Location
- Placement
- Courses

### 🎯 College Predictor
Enter:
- Exam Name
- Rank

Get recommended colleges based on predefined eligibility logic.

### ❤️ Saved Colleges
- Login/Register
- Save favorite colleges
- Manage wishlist

---

# 🛠️ Tech Stack

## Frontend
- React.js
- Tailwind CSS
- React Router
- Axios

## Backend
- Node.js
- Express.js

## Database
- MongoDB
- Mongoose

## Authentication
- JWT
- bcrypt

---

# 📂 Project Structure

```
CollegeListSearch/
│
├── client/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── context/
│   │   └── App.jsx
│
├── server/
│   ├── config/
│   ├── controllers/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   ├── utils/
│   └── server.js
│
├── README.md
└── package.json
```

---

# 📊 Database Collections

### Users
- Name
- Email
- Password
- Saved Colleges

### Colleges
- College Name
- Location
- Fees
- Rating
- Type
- Overview

### Courses
- Course Name
- Duration
- Fees

### Placements
- Average Package
- Highest Package
- Companies Visited

### Reviews
- User Name
- Rating
- Comment

---

# 🌐 REST APIs

## Colleges

```
GET /api/colleges
```

Get all colleges.

```
GET /api/colleges/:id
```

Get a single college.

```
GET /api/colleges/search
```

Search colleges.

```
GET /api/colleges/filter
```

Filter colleges.

---

## Compare

```
GET /api/compare
```

Compare selected colleges.

---

## Predictor

```
POST /api/predict
```

Input:

```json
{
    "exam":"JEE Main",
    "rank":18000
}
```

Output:

```json
[
   "NIT Allahabad",
   "IIIT Lucknow"
]
```

---

## Authentication

```
POST /api/auth/register
```

```
POST /api/auth/login
```

---

## Saved Colleges

```
POST /api/save
```

```
GET /api/save
```

---

# 🎨 UI Pages

- Home
- College Search
- College Details
- Compare Colleges
- College Predictor
- Login
- Register
- Saved Colleges

---

# 📱 Responsive Design

The application is fully responsive and optimized for:
- Desktop
- Tablet
- Mobile

---

# 🔒 Security

- JWT Authentication
- Password Hashing with bcrypt
- Protected Routes
- Input Validation
- Secure REST APIs

---

# ⚡ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/CollegeListSearch.git
```

Move into the project folder.

```bash
cd CollegeListSearch
```

---

## Install Frontend

```bash
cd client
npm install
```

Start the frontend.

```bash
npm run dev
```

---

## Install Backend

```bash
cd server
npm install
```

Start the backend.

```bash
npm run dev
```

---

# 💡 Future Improvements

- AI-based College Recommendation
- College Admission Predictor using Machine Learning
- Student Discussion Forum
- Scholarship Finder
- Email Notifications
- College Reviews with Images
- Dark Mode
- Admin Dashboard

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Arvind Tomar**

GitHub: https://github.com/your-username

LinkedIn: https://linkedin.com/in/your-profile

---

⭐ If you found this project useful, consider giving it a star on GitHub!
