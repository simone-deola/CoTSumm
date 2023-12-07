from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status

from backend.src.definition.input_request import InputsRequest
from backend.src.definition.output_response import OutputRequest
from backend.src.summarization_services import SummarizationService


def create_app(debug=False, **kwargs) -> FastAPI:
    app = FastAPI(debug=False, **kwargs)
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/", status_code=status.HTTP_200_OK)
    async def home():
        return "Home"

    @app.get("/health", status_code=status.HTTP_200_OK, include_in_schema=False)
    async def health():
        return "200"

    @app.post(
        "/summarize",
        status_code=status.HTTP_200_OK,
        description="Endpoint for text summarization",
        response_model=OutputRequest,
        tags=["ENDPOINTS"]
    )
    def summarize_endpoint(input_text: InputsRequest):
        print("s")
        # return OutputRequest(input_text= input_text.text, summary = "summary here", additional_information= ["info here"])
        service = SummarizationService()
        summary, addit_info = service.summarize(input_text.text)
        response = OutputRequest(input_text= input_text.text, summary = summary, additional_information= addit_info)
        return response

    return app


# ---------------------- Endpoints ---------------------- #


if __name__ == "__main__":
    import uvicorn

    app = create_app(debug=True)
    uvicorn.run(
        "server:create_app",
        debug=True,
        reload=True,
        host="0.0.0.0",
        port=8080,
    )
