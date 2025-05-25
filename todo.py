if __name__ == "__main__":
    
    import os
    from todo.main import main
    import logging
    
    BASE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
    LOG_FOLDER_PATH = os.path.join(BASE_DIR_PATH, "logs")
    STORAGE_FOLDER_PATH = os.path.join(BASE_DIR_PATH, "storage")
    
    if not os.path.exists(STORAGE_FOLDER_PATH):
        os.makedirs(STORAGE_FOLDER_PATH, exist_ok=True)
        
        storage_file = os.path.join(STORAGE_FOLDER_PATH, "storage.json")
        
        if not os.path.exists(storage_file):
            with open(storage_file, "w", encoding="utf-8") as f:
                f.write("[]")
    
    if not os.path.exists(LOG_FOLDER_PATH):
        os.makedirs(LOG_FOLDER_PATH, exist_ok=True)

        log_file = os.path.join(LOG_FOLDER_PATH, "app.log")

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # 중복 핸들러 방지
        if not logger.handlers:
            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
    
    main()