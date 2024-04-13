from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import bp_endpoints, mag_endpoints

import config

app = FastAPI(docs_url=config.documentation_url)

app.include_router(router=mag_endpoints.app, prefix="/mag")
app.include_router(router=bp_endpoints.app, prefix="/bp")

origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    # todo: aan te passen na hosting
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





