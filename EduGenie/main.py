from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import generate_learning_path


app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0",
)


# Static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")


# Request model
class QuestionRequest(BaseModel):
    question: str


# Home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )


# Health check
@app.get("/health")
def health():
    return {
        "status": "ok",
        "app": "EduGenie",
    }


# Q&A
@app.post("/qa")
def qa(request: QuestionRequest):
    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty.",
        )

    try:
        answer = answer_question(question)

        return {
            "question": question,
            "answer": answer,
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        )


# Explanation
@app.post("/explain")
def explain(request: QuestionRequest):
    topic = request.question.strip()

    if not topic:
        raise HTTPException(
            status_code=400,
            detail="Topic cannot be empty.",
        )

    try:
        explanation = explain_topic(topic)

        return {
            "topic": topic,
            "explanation": explanation,
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        )


# Quiz
@app.post("/quiz")
def quiz(request: QuestionRequest):
    topic = request.question.strip()

    if not topic:
        raise HTTPException(
            status_code=400,
            detail="Topic cannot be empty.",
        )

    try:
        quiz_data = generate_quiz(topic)

        return quiz_data.model_dump()

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        )


# Summarization
@app.post("/summarize")
def summarize(request: QuestionRequest):
    text = request.question.strip()

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty.",
        )

    try:
        summary = summarize_text(text)

        return {
            "text": text,
            "summary": summary,
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        )


# Learning Path
@app.post("/learn/recommendations")
def learning_recommendations(request: QuestionRequest):
    topic = request.question.strip()

    if not topic:
        raise HTTPException(
            status_code=400,
            detail="Topic cannot be empty.",
        )

    try:
        learning_path = generate_learning_path(topic)

        return {
            "topic": topic,
            "learning_path": learning_path,
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        )