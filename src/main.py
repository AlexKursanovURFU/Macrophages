from loguru import logger
from states import init_model_parameters

# Настройка логгера
logger.add("model.log", rotation="1 MB", level="INFO", 
           format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")

def main():
    """Основная функция модели."""
    logger.info("Начало инициализации модели")

    # Инициализация состояний и констант
    states, constants = init_model_parameters()
    logger.success(f"Инициализация завершена ({len(states)} состояний, {len(constants)} констант)")

if __name__ == "__main__":
    main()