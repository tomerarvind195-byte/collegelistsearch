# 🎓 CollegeFind — College Listing & Search Web Application

> A modern college discovery platform that helps students search, compare, and explore colleges across India — built with HTML5, CSS3, JavaScript, and Python.

![HTML5](https://img.shields.io/badge/HTML5-91.5%25-E34F26?style=flat&logo=html5)
![Python](https://img.shields.io/badge/Python-8.5%25-3776AB?style=flat&logo=python)
![CSS3](https://img.shields.io/badge/CSS3-Styled-1572B6?style=flat&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=flat&logo=javascript)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat)
![Commits](https://img.shields.io/badge/Commits-8-blue?style=flat)

---

## 🔗 Live Demo

> 🌐 **[******]** 

---

## 📸 Screenshots

| Home Page | College Listing | Compare Colleges |
| :---: | :---: | :---: |
| <img src="https://github.com/user-attachments/assets/db2dfade-16f4-4ed0-b4d9-36b343da11d8" width="100%" alt="Home Page" /> | <img src="https://github.com/user-attachments/assets/150a6fd1-f725-4650-b41b-8bb93af6ab27" width="100%" alt="College Listing" /> | <img src="https://github.com/user-attachments/assets/f018a78c-4761-4ebc-949e-c2e228c4413b" width="100%" alt="Compare Colleges" /> |

---

## 📋 About The Project

**CollegeFind** is a production-oriented college discovery web application designed to simplify the college selection process for students across India. Students can search, filter, compare, and evaluate colleges based on fees, ratings, placements, and location — all in one place.

**Inspired by:** Platforms like Shiksha, Collegedunia, and CollegeDekho — built from scratch as a full-featured MVP.

**Key Highlights:**
- 4 fully functional pages — Home, College Listing, Compare, Predictor.
- Search by college name, course, location, fees, rating, and stream.
- College Predictor — recommends colleges based on exam name and rank
- Compare up to 3 colleges side-by-side
- Fully responsive design — works on mobile, tablet, and desktop

---

## ✨ Features

### 🏠 Home Page
- Hero section with prominent search bar.
- Popular college categories section.
- Compare Colleges quick access.
- College Predictor section.
- Fully responsive navigation and footer.

### 🔍 College Listing & Search
- Search colleges by **name** or **course**
- Filter by **Stream**, **Annual Fees**, **Location**, **Rating**, **College Type**
- Sorting options (by rating, fees, name)
- Pagination for smooth browsing
- Responsive card layout showing:
  - College Name & Location
  - Annual Fees & Rating
  - Available Courses
  - Save · Compare · View Details buttons

### 🎯 College Predictor
- Student enters **Exam Name** (JEE, NEET, JEECUP, etc.) and **Rank**.
- System recommends best-fit colleges based on rank cutoffs.
- Helps students make data-driven admission decisions.

### ⚖️ Compare Colleges
- Select up to **3 colleges** simultaneously
- Side-by-side comparison of:
  - Fees · Ratings · Placements · Location
- Helps students make informed final decisions

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, JavaScript (ES6) |
| Backend | Python |
| Planned Backend | Python, Django REST Framework |
| Planned Database | MySQL |
| Planned Auth | Django Authentication |
| Deployment | GitHub Pages / Netlify _(add your link)_ |
| Version Control | Git & GitHub |

---

## 📁 Project Structure Details

```
College_list_search-WebApplication/
│
├── Collegelist/                  # Main project folder
│   ├── index.html                # Home Page
│   ├── college.html              # College Detail Page
│   ├── compare.html              # Compare Colleges Page
│   ├── predictor.html            # College Predictor Page  and other 
│   │
│   ├── css/
│   │   └── style.css             # Main stylesheet
│   │
│   └── js/
│       ├── app.js                # Main app logic
│       ├── search.js             # Search & filter logic
│       ├── filter.js             # Filter handling
│       └── compare.js            # Compare functionality
│
├── env/                          # Environment configuration
├── README.md
└── backend/ (planned)
    ├── routes/
    ├── models/
    ├── controllers/
    └── server.js
```

---

## 🚀 Getting Started

### Option 1 — Open directly in browser (Quickest)

```bash
# 1. Clone the repository
git clone https://github.com/tomerarvind195-byte/College_list_search-WebApplication.git
cd College_list_search-WebApplication/Collegelist

# 2. Open index.html in your browser
# Just double-click index.html — no setup needed!
```

### Option 2 — Run with Python local server

```bash
# Navigate to project folder
cd College_list_search-WebApplication/Collegelist

# Start Python local server
python -m http.server 8000

# Open in browser
# http://localhost:8000
```

### Option 3 — Deploy on GitHub Pages (Free hosting)

```bash
# 1. Push your code to GitHub (already done!)
# 2. Go to repo Settings → Pages
# 3. Source: Deploy from branch → main → /Collegelist
# 4. Your site will be live at:
#    https://tomerarvind195-byte.github.io/College_list_search-WebApplication/
```

---

## 🗺️ Pages Overview

| Page | File | Description |
|------|------|-------------|
| 🏠 Home | `index.html` | Landing page with search & categories |
| 🔍 College Listing | `college.html` | Search, filter & browse colleges |
| ⚖️ Compare | `compare.html` | Compare up to 3 colleges side-by-side |
| 🎯 Predictor | `predictor.html` | Get college recommendations by rank |

---

## 🔮 Future Improvements

- [ ] **User Authentication** — Login/Signup with Django Auth
- [ ] **Save Favourite Colleges** — Bookmark colleges for later
- [ ] **Real Database Integration** — MySQL with live college data via Django ORM
- [ ] **AI-based College Recommendation** — ML model based on marks, interests, budget
- [ ] **Placement Analytics** — Average salary, top recruiters per college
- [ ] **Admission Alerts** — Notify users about deadlines and cutoffs
- [ ] **Discussion Forum** — Q&A section for students
- [ ] **Backend API** — Django REST Framework (DRF) API
- [ ] **Mobile App** — Progressive Web App (PWA) version

---

## 🎯 Project Objective

The goal of CollegeFind is to simplify the college selection process by providing students with an easy-to-use platform where they can search, compare, and evaluate colleges based on important factors like fees, ratings, placements, and location — all in one place, for free.

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/college-predictor-ml`)
3. Commit your changes (`git commit -m 'Add ML-based predictor'`)
4. Push to the branch (`git push origin feature/college-predictor-ml`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Arvind Kumar**
3rd Year B.Tech IT Student | Aspiring Software Engineer

- 🌐 [LinkedIn](https://www.linkedin.com/in/arvind-kumar-399a60338)
- 💻 [GitHub](https://github.com/tomerarvind195-byte)
- 📧 tomerarvind195@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> ⭐ Agar CollegeFind helpful laga toh **star** zaroor karo — ek star bahut motivation deta hai! 🙏
