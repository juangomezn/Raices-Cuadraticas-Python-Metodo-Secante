# 📐 Resolución de Ecuaciones Cuadráticas en Python

Este proyecto implementa la solución de ecuaciones cuadráticas de la forma `ax² + bx + c = 0` utilizando dos métodos:

1. **Fórmula General** (para obtener una raíz real exacta si el discriminante lo permite).
2. **Método de la Secante** (para encontrar una segunda raíz real aproximada mediante un método numérico iterativo).

---

## 🧮 ¿Cómo funciona?

1. **Entrada de datos:**
   El programa solicita al usuario ingresar los valores de los coeficientes `a`, `b` y `c`.

2. **Validación inicial:**
   - Si `a = 0`, el programa indica que no se trata de una ecuación cuadrática.
   - Si el discriminante (`b² - 4ac`) es menor que 0, no existen soluciones reales.

3. **Cálculo de la primera raíz (x₁):**
   Se calcula usando la **fórmula general**:

   \[
   x_1 = \frac{-b - \sqrt{b^2 - 4ac}}{2a}
   \]

4. **Cálculo de la segunda raíz (x₂):**
   Se obtiene mediante el **método de la secante**, utilizando valores iniciales `x₀ = -0.6` y `x₁ = -0.5`, iterando hasta alcanzar una tolerancia de `0.0001` o un máximo de `1000` iteraciones.

---

## ▶️ Cómo ejecutar el programa

Asegúrate de tener Python instalado. Luego, ejecuta el script con:

```bash
python nombre_del_archivo.py
```

Sigue las instrucciones en pantalla para ingresar los coeficientes de la ecuación cuadrática.

---

## 🧪 Ejemplo de salida

```
Ingrese Valor de a: -2.5
Ingrese Valor de b: 15.5
Ingrese Valor de c: 10
X1 (Fórmula Cuadrática) = -0.701
X2 (Secante) = -5.697
Iteraciones: 5
```

---

## 📌 Requisitos

- Python 3.x
- Módulo estándar `math`

---

## ✅ Ventajas del uso de métodos numéricos

- Permite encontrar soluciones cuando no se puede aplicar directamente una fórmula.
- Ofrece aproximaciones útiles en contextos donde se requiere precisión controlada.
- Es útil para aprender técnicas de análisis numérico como la **secante** o **Newton-Raphson**.

---


## 📜 Licencia [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) 

<div style="
    background: linear-gradient(90deg, #e8e8e8 100%);
    border-left: 4px solid #3498db;
    padding: 1rem;
    border-radius: 4px;
    margin: 1rem 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
">

Este proyecto está licenciado bajo **Apache License 2.0**.  
Para más información, consulta el archivo [LICENSE](LICENSE) o visita [apache.org/licenses](https://www.apache.org/licenses/LICENSE-2.0).
</div>

<h2>
  ✨ Elaborado por
  <img src="https://img.shields.io/badge/Juan%20David%20Gomez-black?style=for-the-badge&logo=dev.to&logoColor=white" alt="Author" style="vertical-align: middle; margin-left: 8px;">
</h2>

[![GitHub](https://img.shields.io/badge/GitHub-JuanDavidGomezN-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/juangomezn)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-JuanDavidGomezN-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/juangomezn)

[![Gmail](https://img.shields.io/badge/Gmail-juan.david%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gomezninoj681@gmail.com)
