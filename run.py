from app import app, logger

if __name__ == "__main__":
    logger.info("Application was started.")
    app.run(host = '0.0.0.0')
