# Описание проекта
Целью проекта является построение модели для прогнозирования цен на подержанные автомобили. В качестве исходных данных используется набор из Kaggle: [Car Price Prediction Dataset](https://www.kaggle.com/datasets/vijayaadithyanvg/car-price-predictionused-cars/data).

# Запуск
Для запуска проекта выполните следующие команды:

1. Клонируйте репозиторий:
   ```bash
   git clone <repository_url>
   cd <repository_folder>

2.	Установите и активируйте виртуальное окружение:
python -m venv .venv_my_proj
source .venv_my_proj/bin/activate  # для MacOS/Linux
.\.venv_my_proj\Scripts\activate   # для Windows

3.	Установите необходимые зависимости:
pip install -r requirements.txt

4.	Запустите MLFlow сервер:
	•	Скрипт находится в корне проекта.
	•	Выполните команду: 
    mlflow server --backend-store-uri sqlite:///mlruns.db --default-artifact-root ./mlruns --host 127.0.0.1 --port 5001

# Результаты исследования
Лучшая модель

По итогам исследования лучшая модель — это Random Forest Regressor. Она была обучена с использованием оптимальных гиперпараметров, подобранных с помощью библиотеки Optuna:
	•	n_estimators: 150
	•	max_depth: 20
	•	max_features: 0.8

Результаты метрик на тестовой выборке:

	•	Mean Absolute Error (MAE): 0.485
	•	Mean Absolute Percentage Error (MAPE): 0.223
	•	Mean Squared Error (MSE): 0.610

# Выбранные признаки

В итоговой модели использовались следующие признаки:
	•	Числовые:
	•	Year
	•	Present_Price
	•	Driven_kms
	•	Категориальные (после обработки OneHotEncoder):
	•	Car_Name
	•	Fuel_Type
	•	Selling_type
	•	Transmission

# Run ID

Модель с лучшими параметрами была залогирована в MLflow. Run ID лучшей модели: 5627ba29c4fd4ae18a98e2b8d085ac00.

Модель зарегистрирована как четвертая версия (v4) с именем: RandomForestModel.

# Запуск MLFlow
Для проверки результатов и экспериментов:
	1.	Запустите сервер MLFlow:
    mlflow server --backend-store-uri sqlite:///mlruns.db --default-artifact-root ./mlruns --host 127.0.0.1 --port 5001
	2.	Откройте интерфейс в браузере:
    http://127.0.0.1:5001
    3.	Найдите нужный эксперимент по имени или идентификатору Run ID.