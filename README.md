# Serverless API Management System

A RESTful API built with AWS Lambda, API Gateway, DynamoDB, and Python.

## Architecture
Client → API Gateway → Lambda (Python) → DynamoDB

## Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /items | Get all items (sorted by name) |
| GET | /items?category=electronics | Filter items by category |
| POST | /items | Create a new item |
| PUT | /items/{id} | Update an existing item |
| DELETE | /items/{id} | Delete an item |

## Authentication
All endpoints require an API key passed in the request header:
x-api-key: YOUR_API_KEY_HERE

## Features
- Full CRUD operations
- Search by category
- Input validation
- API key authentication
- CloudWatch logging

## Tech Stack
- AWS Lambda (Python 3.12)
- AWS API Gateway
- AWS DynamoDB
- AWS CloudWatch
