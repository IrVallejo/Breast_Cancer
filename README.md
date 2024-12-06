# Análisis Comparativo de Algoritmos de Machine Learning en la Predicción del Cáncer de Mama

# **Predicción de Cáncer de Mama usando Machine Learning**

Este proyecto compara el desempeño de tres algoritmos de Machine Learning (Decision Tree, Random Forest y Gradient Boosting) en la predicción del cáncer de mama, utilizando métricas clave como precisión, sensibilidad, especificidad y F1-score. Los resultados obtenidos ofrecen una base sólida para identificar el modelo más adecuado en contextos clínicos.

---

## **Tabla de Contenidos**
- [Introducción](#introducción)
- [Dataset](#dataset)
- [Algoritmos Utilizados](#algoritmos-utilizados)
- [Métricas de Evaluación](#métricas-de-evaluación)
- [Resultados](#resultados)
- [Requisitos](#requisitos)
- [Instrucciones de Uso](#instrucciones-de-uso)
- [Conclusión](#conclusión)
- [Contribuciones](#contribuciones)

---

## **Introducción**

El cáncer de mama es una de las principales causas de muerte en mujeres a nivel mundial. Este proyecto utiliza técnicas de Machine Learning para ayudar en la detección temprana del cáncer, maximizando la sensibilidad y precisión para minimizar errores en el diagnóstico.

## **Dataset**

El dataset utilizado es el **Wisconsin Breast Cancer Dataset**, ampliamente reconocido en el ámbito de Machine Learning, que incluye características extraídas de imágenes digitales de biopsias.  
[Más información sobre el dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#wisconsin-breast-cancer-dataset).

### **Características Principales:**
- 30 variables predictoras relacionadas con características de las células.
- Etiquetas de salida: *Benigno* o *Maligno*.

---

## **Algoritmos Utilizados**

Se evaluaron los siguientes modelos:
1. **Decision Tree**: Modelo básico basado en reglas jerárquicas.
2. **Random Forest**: Conjunto de árboles de decisión con mejor capacidad generalizadora.
3. **Gradient Boosting**: Modelo avanzado basado en boosting para minimizar el error iterativamente.

---

## **Métricas de Evaluación**

Se usaron las siguientes métricas para comparar los modelos:
- **Accuracy (Precisión)**: Proporción de predicciones correctas.
- **ROC AUC**: Capacidad del modelo para distinguir entre clases.
- **Precision (Precisión Positiva)**: Proporción de positivos verdaderos entre todos los predichos como positivos.
- **Recall (Sensibilidad)**: Proporción de casos positivos correctamente identificados.
- **F1-Score**: Promedio armónico entre precisión y sensibilidad.

---

## **Resultados**

| Modelo             | Accuracy | ROC AUC | Precision | Recall | F1-Score |
|--------------------|----------|---------|-----------|--------|----------|
| Decision Tree      | 90.35%   | 0.8988  | 86.05%    | 88.10% | 87.06%   |
| Random Forest      | 93.86%   | 0.9315  | 92.68%    | 90.48% | 91.57%   |
| Gradient Boosting  | 94.74%   | 0.9484  | 90.91%    | 95.24% | 93.02%   |

---

## **Requisitos**

- Python 3.8 o superior
- Bibliotecas necesarias:
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`

---

## **Instrucciones de Uso**

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/prediccion-cancer-mama.git
   cd prediccion-cancer-mama
git