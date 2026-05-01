"""
Create a React application with a UserCard component to display user information, a list page showing a collection of UserCard components, and a detail page with additional user details, fetching the user data from an external API
"""
import httpx
import asyncio 
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel, EmailStr 
from typing import Optional

app = FASTAPI(title="title", version="1.0.0")

app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:3000"],
	allow_methods=["GET"],
	allow_headers=["*"])

EXTERNAL_API = "https://jsonplaceholder.typicode.com"

class Address(BaseModel):
	street: str 
	suite: str 
	city: str 
	zipcode: str 

class Company(BaseModel):
	name: str 
	bs: str 
	catchPhrase: str

class UserSummary(BaseModel):
	id: int 
	name: str 
	username: str 
	email: str 
	phone: str 
	website: str 
	address: Address
	company: Company 

class UserDetail(BaseModel):
	id: int 
	name: str 
	username: str 
	email: str 
	phone: str 
	website: str 
	address: Address 
	company: Company 
	posts: list[Post]
	post_count: int

class Post(BaseModel):
	id: int 
	userid: int 
	title: str 
	body: str 

async def get_client():
	async with httpx.AsyncClient(timeout=10.0) as client:
		yield client

@app.get("/users", response_model=list[UserSummary])
async def list_users():
	async with httpx.AsyncClient(timeout=10.0) as client:
		response = await client.get(f"{EXTERNAL_API}/users")

	if response.status_code != 200:
		raise HTTPException(
			status_code=502,
			detail="Failed to fetch users from upstream API")

	return response.json()

@app.get("/users/{user_id}",response_model=UserDetail)
async def get_user(user_id: int):
	async with httpx.AsyncClient(timeout=0.0) as client:
		user_response, posts_response = await asyncio.gather(
			client.get(f"{EXTERNAL_API}/users/{user_id}"),
			client.get(f"{EXTERNAL_API}/posts?userId={user_id}")
			)

	if user_response.status_code == 404:
		raise HTTPException(status_code=404, detail=f"user {User_id} not found")

	if user_response.status_code != 200:
		raise HTTPException(status_code=502, detail=f"Upstream API Error")

	user_data = user_response.json()
	posts_data = posts_response.json() if posts_response.status_code==200 else []

	return {
	**user_data, 
	"posts": posts_data,
	"posts_count": len(posts_data)
	}

@app.get("/users/{user_id}/posts", response_model=list[Post])
async def get_user_posts(user_id: int, limit: int = 10):
	async with httpx.AsyncClient(timeout=10.0) as client:
		response = await client.get(
			f"{EXTERNAL_API}/posts",
			params={"userId": user_id}
			)

	posts = response.json()
	return posts[:limit]

@app.get("/health")
async def health():
	return {"status":"ok", "version":"1.0.0"}