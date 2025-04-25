# Sessionizer — Разметка пользовательских сессий

## 📌 Описание

Скрипт обрабатывает DataFrame с логами просмотров товаров на сайте и размечает сессии пользователей.  
Сессией считается последовательность действий одного пользователя, между которыми прошло не более **3 минут** (или другого заданного значения).

## 📥 Входные данные

DataFrame со столбцами:

- `customer_id` — ID пользователя
- `product_id` — ID просмотренного товара
- `timestamp` — время просмотра

## 📤 Выходные данные

К исходному DataFrame добавляются:

- `session_id` — номер сессии пользователя
- `global_session_id` — уникальный ID сессии в формате `customerID_sessionID`

## Шаг 3: Обновите pip

```bash
python -m pip install --upgrade pip
```

## Шаг 4: Установите зависимости

```bash
pip install -r requirements.txt
```
## ✅ Запуск

```bash
python sessionizer.py
```

## ▶ Пример

```python
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
```

### 👨‍💻 Автор
## Новаев Денис
## Telegram: @m1dden