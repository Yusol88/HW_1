# app/utils/validators.py
class DataValidator:
    @staticmethod
    def validate_prediction_data(data: dict) -> ValidationResult:

        # Проверка структуры данных
   