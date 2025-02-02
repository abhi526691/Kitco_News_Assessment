from fastapi import FastAPI
from api.routes.articles import router as article_router
from api.middleware import add_security_headers, add_cors
from core.logging_config import configure_logging

app = FastAPI(title="Kitco Management System")

# Add middleware
add_cors(app)
app.middleware("http")(add_security_headers)

# Include routes
app.include_router(article_router, prefix="/articles", tags=["Articles"])

# Configure logging
configure_logging()
