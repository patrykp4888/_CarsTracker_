from flask import Flask, request
from web.celery_queue import scraping_task


app = Flask(__name__)


@app.route("/scrape", methods=["POST"])
def scrape():
    """
    Request attributes:
        Header: {"Content-Type": "application/json"}
        Body: {
            "brand": <value>,
            "model": <value>,
            "min_production_year": <value> (optional),
            "min_price": <value> (optional),
            "max_price": <value> (optional),
            "max_production_year": <value> (optional),
            "min_mileage": <value> (optional),
            "max_mileage": <value> (optional),
        }
    """

    attrs = request.json

    task_info = scraping_task.delay(attrs)

    return {"status": "triggered", "task_id": task_info.id}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)
