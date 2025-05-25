from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Sample student marks data (100 students)
student_marks = {
    "Alice": 85, "Bob": 72, "Charlie": 90, "Diana": 68, "Eve": 95,
    "Frank": 78, "Grace": 88, "Henry": 62, "Ivy": 91, "Jack": 77,
    # ... (add more names as needed)
}

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    return {"marks": [student_marks.get(name, 0) for name in names]}
