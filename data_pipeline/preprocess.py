import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

def load_and_preprocess_data(csv_path: str):
    # 1. Carga de datos
    df = pd.read_csv(csv_path)
    print(f"Dimensiones iniciales: {df.shape}")

    # 2. Manejo de valores nulos (si existen)
    df = df.dropna()

    # 3. Separación de características (X) y variable objetivo (y)
    # Ajustar 'clasificacion_cognitiva' al nombre exacto de la columna target en tu CSV
    target_col = 'clasificacion_cognitiva'
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # 4. Codificación One-Hot para variables categóricas
    # (Sexo, Residencia, Alcohol, Tabaco, Actividad física, Antecedentes)
    cat_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
    X_encoded = pd.get_dummies(X, columns=cat_cols, drop_first=True)

    # 5. División estratificada (Train 80% / Test 20%) antes de SMOTE para evitar data leakage
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=0.2, random_state=42, stratify=y
    )

    # 6. Escalado de variables numéricas
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Distribución de clases en Train antes de SMOTE:")
    print(y_train.value_counts())

    # 7. Balanceo sintético con SMOTE solo en el conjunto de entrenamiento
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train_scaled, y_train)

    print("Distribución de clases en Train después de SMOTE:")
    print(pd.Series(y_train_resampled).value_counts())

    return X_train_resampled, X_test_scaled, y_train_resampled, y_test, scaler

if __name__ == "__main__":
    # Ruta de prueba
    data_path = "raw_data/moca_dataset.csv"
    try:
        X_tr, X_te, y_tr, y_te, scaler = load_and_preprocess_data(data_path)
        print("\nPreprocesamiento completado exitosamente.")
    except FileNotFoundError:
        print(f"\nArchivo no encontrado en '{data_path}'. Coloca el CSV en esa ruta.")