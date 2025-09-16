📸 Instagram Clone API

A backend API that mimics Instagram's core functionality — allowing users to register, log in, and post images. This project is built with Python and structured into modular components for easy maintenance and scalability.

---

#🧰 Tech Stack

- Language: Python 3
- Framework: FastAPI
- Database: File-based ( SQLite in `ig_api_db`)
- Image Storage: Local filesystem (`/images`)
- Auth: Custom login/register logic (`auth/`)
- Routing: Modular routing via `routers/`

---

📁 Project Structure

Instagram-Clone-Api/
├── auth/ # User authentication logic
├── db/ # DB setup 
├── ig_api_db/ # Database files or schema
├── images/ # Uploaded images
├── routers/ # API route definitions
├── main.py # Entry point
├── requirements.txt # Python dependencies



🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Manishkumar29/Instagram-Clone-Api.git
cd Instagram-Clone-Api
2. Set Up Virtual Environment
bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the Server
bash
Copy code
python main.py
🔌 Example API Endpoints
Method	Endpoint	Description
POST	/auth/register	Register a new user
POST	/auth/login	Login and get credentials
GET	/posts/	Get all posts
POST	/posts/	Create a new post
DELETE	/posts/{id}	Delete a post

These may vary based on actual implementation.

🧪 Testing
Manually test via:

 Postman

 curl

 Browser (for GET endpoints)

🚧 Future Enhancements
 JWT Authentication

 Cloud image storage (e.g. S3 or Cloudinary)

 Use PostgreSQL or MongoDB

 Pagination, likes & comments

 Dockerization

 CI/CD for deployment

📄 License
MIT License

👨‍💻 Author
Made with 💻 by @Manishkumar29

yaml
Copy code

---

You can now copy this and save it as `README.md` in the root of your project directory, then commit and push it:

```bash
git add README.md
git commit -m "Add project README"
git push origin main
