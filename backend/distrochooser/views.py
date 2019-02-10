from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from distrochooser.models import UserSession, Question, Category, Answer
import secrets
from distrochooser.constants import TRANSLATIONS
from backend.settings import LOCALES
from django.forms.models import model_to_dict
from json import dumps

def jsonResponse(data):
  response = JsonResponse(data)
  response["Access-Control-Allow-Origin"] = "*"
  response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
  return response

def jumpToQuestion(index: int) -> Question:
  results = Question.objects.filter(category__index=index)
  if results.count() == 0:
    raise Exception("Question unknown")
  return results.get()

def goToStep(categoryIndex: int) -> dict:
  results = Question.objects.filter(category__index=categoryIndex)
  if results.count() == 0:
    raise Exception("Question unknown")
  question = results.first()
  answers = Answer.objects.filter(question=question)
  return {
    "question": model_to_dict(question, fields=('id', 'msgid')),
    "category": model_to_dict(question.category),
    "answers":  list(answers.values("msgid"))
  }

def start(request: HttpRequest, langCode: str):
  """
  'Loggs' the visitor in, creates a session which will be used to store the user's action.
  """
  if langCode not in LOCALES:
    raise Exception("Language not installed")

  userAgent = request.META["HTTP_USER_AGENT"]
  session = UserSession()
  session.userAgent = userAgent
  session.token = secrets.token_hex(5) # generate a random token for the user
  session.save()


  questionAndCategoryData = goToStep(0)
  return jsonResponse({
    "token": session.token,
    "translation": TRANSLATIONS["de-de"],
    "question": questionAndCategoryData["question"],
    "category": questionAndCategoryData["category"],
    "categories": list(Category.objects.all().values()),
    "answers": questionAndCategoryData["answers"]
  })