mlflow server --backend-store-uri sqlite:///mlruns.db  

mlflow db upgrade sqlite:///mlruns.db     

uvicorn main:app --reload 