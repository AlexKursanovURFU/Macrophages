from scipy.integrate import odeint
from parameters import init_consts
from model import computeRates

sizeStates = 29
sizeConstants = 58

def solve_model(
    simulation_time=20.0, 
    num_points=10000,
    initial_states=None,
    constants=None,
    solver='odeint',
    rtol=1.0e-7,
    atol=1.0e-7,
    verbose=True
):
    """Решает модель сердечной клетки с использованием ODE-решателя.
    
    Параметры:
        simulation_time (float): Длительность симуляции в секундах (по умолчанию 20)
        num_points (int): Количество точек для вывода (по умолчанию 10000)
        initial_states (array-like): Начальные состояния (если None, используются значения по умолчанию)
        constants (array-like): Параметры модели (если None, используются значения по умолчанию)
        solver (str): Используемый решатель ('odeint' или 'solve_ivp')
        rtol (float): Относительный допуск для решателя
        atol (float): Абсолютный допуск для решателя
        verbose (bool): Выводить информацию о ходе решения
        
    Возвращает:
        tuple: (voi, states) - массив временных точек и соответствующих состояний
    """
    try:
        from scipy.integrate import odeint, solve_ivp
        import numpy as np
        
        # Инициализация параметров модели
        if constants is None or initial_states is None:
            default_states, default_constants = initConsts()
            if constants is None:
                constants = default_constants
            if initial_states is None:
                initial_states = default_states

        # Проверка входных данных
        initial_states = np.asarray(initial_states, dtype=np.float64)
        constants = np.asarray(constants, dtype=np.float64)
        
        if len(initial_states) != sizeStates:
            raise ValueError(f"Размер initial_states должен быть {sizeStates}")
        if len(constants) != sizeConstants:
            raise ValueError(f"Размер constants должен быть {sizeConstants}")

        # Создание временной сетки
        voi = np.linspace(0, simulation_time, num_points)
        
        if verbose:
            print(f"Running simulation for {simulation_time} seconds with {num_points} points")
            print(f"Using solver: {solver}")

        # Выбор и запуск решателя
        if solver == 'odeint':
            # Использование odeint
            states = odeint(
                func=computeRates,
                y0=initial_states,
                t=voi,
                args=(constants,),
                rtol=rtol,
                atol=atol,
                tfirst=True
            )
        elif solver == 'solve_ivp':
            # Использование solve_ivp (более современный вариант)
            solution = solve_ivp(
                fun=lambda t, y: computeRates(y, t, constants),
                t_span=(0, simulation_time),
                y0=initial_states,
                t_eval=voi,
                method='LSODA',
                rtol=rtol,
                atol=atol
            )
            states = solution.y.T
        else:
            raise ValueError(f"Неизвестный решатель: {solver}. Доступные варианты: 'odeint', 'solve_ivp'")

        if verbose:
            print("Simulation completed successfully")

        return voi, states

    except ImportError as e:
        raise ImportError("Для работы solve_model требуется scipy. Установите его: pip install scipy") from e
    except Exception as e:
        raise RuntimeError(f"Ошибка при решении модели: {str(e)}") from e