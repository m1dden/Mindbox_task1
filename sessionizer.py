import pandas as pd


def add_session_id(
        df: pd.DataFrame, session_threshold_minutes: int = 3
) -> pd.DataFrame:
    # Убедимся, что timestamp в формате datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Сортировка по customer_id и timestamp
    df = df.sort_values(by=['customer_id', 'timestamp'])

    # Вычисляем разницу во времени между текущим и предыдущим просмотром в группе по customer_id
    df['time_diff'] = df.groupby('customer_id')['timestamp'].diff()

    # Отмечаем, где начинается новая сессия: либо первый просмотр, либо разница > порог в минутах
    df['new_session'] = (
        df['time_diff'].isna()
        | (df['time_diff'] > pd.Timedelta(minutes=session_threshold_minutes))
    )

    # Считаем session_id — накопительное число новых сессий в пределах одного customer_id
    df['session_id'] = df.groupby('customer_id')['new_session'].cumsum().astype(int)

    # Создаем глобальный уникальный ID сессии для удобства (опционально)
    df['global_session_id'] = (
        df['customer_id'].astype(str) + '_' + df['session_id'].astype(str)
    )

    # Удаляем временные столбцы
    df = df.drop(columns=['time_diff', 'new_session'])

    return df


if __name__ == "__main__":
    # Пример использования
    data = {
        'customer_id': [1, 1, 1, 2, 2],
        'product_id': [10, 11, 12, 20, 21],
        'timestamp': [
            '2024-01-01 10:00:00',
            '2024-01-01 10:02:00',
            '2024-01-01 10:10:00',
            '2024-01-01 11:00:00',
            '2024-01-01 11:02:30',
        ]
    }
    df = pd.DataFrame(data)
    df_with_sessions = add_session_id(df)
    print(df_with_sessions)
