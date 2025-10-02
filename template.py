import os
from pathlib import Path

projet_name = "us_visa"

list_of_files = [
    f"{projet_name}/__init__.py",
    f"{projet_name}/components/__init__.py",
    f"{projet_name}/components/data_ingestion.py",
    f"{projet_name}/components/data_validation.py",
    f"{projet_name}/components/data_transformation.py",
    f"{projet_name}/components/model_trainer.py",
    f"{projet_name}/components/model_evaluation.py",
    f"{projet_name}/components/model_pusher.py",
    f"{projet_name}/configuration/__init__.py",
    f"{projet_name}/constants/__init__.py",
    f"{projet_name}/entity/__init__.py",
    f"{projet_name}/entity/config_entity.py",
    f"{projet_name}/entity/artifact_entity.py",
    f"{projet_name}/exception/__init__.py",
    f"{projet_name}/logger/__init__.py",
    f"{projet_name}/pipeline/__init__.py",
    f"{projet_name}/tarining_pipeline/__init__.py",
    f"{projet_name}/prediction_pipeline/__init__.py",
    f"{projet_name}/utils/__init__.py",
    f"{projet_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "setup.py",
    "confg/model.yaml",
    "confg/schema.yaml",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    print(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"{filename} is already present in {filedir} and has some content, skipping file creation")