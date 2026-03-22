# Sistema de Control de Costes

El control de costes es la disciplina que diferencia un restaurante rentable de uno que cierra en los primeros 3 años. Este documento detalla las metodologías para calcular el coste real de cada plato, gestionar mermas, controlar inventario y aplicar ingeniería de menú para maximizar la rentabilidad.

---

## 1. Cálculo del coste de plato (receta valorada)

### 1.1 Concepto

El **coste de plato** es la suma del coste de cada ingrediente que compone un plato, valorado al precio de compra real. No es una estimación: es un cálculo preciso basado en las quantities reales de cada componente.

### 1.2 Proceso paso a paso

#### Paso 1: Definir la receta estándar (estándar de producción)

Cada plato debe tener una **ficha técnica** con:

- Lista completa de ingredientes con cantidades exactas (gramos, ml).
- Procedimiento de elaboración detallado.
- Peso bruto y peso neto del plato terminado.
- Emplatado, decoración y presentación.
- Tiempo de elaboración.
- Temperatura objetivo de servicio.

#### Paso 2: Valorar cada ingrediente

```
Coste del ingrediente = Precio de compra / Cantidad comprada × Cantidad usada
```

Ejemplo para 1 kg de solomillo de cerdo a 14 €/kg:

```
Coste de 180 g de solomillo = 14 / 1.000 × 180 = 2,52 €
```

#### Paso 3: Sumar todos los ingredientes

Incluye no solo los ingredientes principales, sino también:

- Aceites y grasas de cocción
- Salsas y fondos (calculados como coste por ración)
- Especias y especias (aunque sean small quantities, se acumulan)
- Guarniciones valoradas individualmente

#### Paso 4: Calcular el coste total del plato

```
Coste total del plato = Σ (coste de cada ingrediente)
```

#### Paso 5: Calcular el food cost del plato

```
Food cost (%) = (Coste del plato / Precio de venta) × 100
```

### 1.3 Ejemplo práctico: Solomillo de cerdo al Pedro Ximénez

| Ingrediente | Cantidad | Precio compra | Coste |
|---|---|---|---|
| Solomillo de cerdo | 180 g | 14 €/kg | 2,52 € |
| Aceite de oliva | 15 ml | 8 €/l | 0,12 € |
| Cebolla | 50 g | 1,20 €/kg | 0,06 € |
| Zanahoria | 30 g | 1 €/kg | 0,03 € |
| Puerro | 20 g | 1,50 €/kg | 0,03 € |
| Fondo oscuro | 100 ml | 3 €/l | 0,30 € |
| Pedro Ximénez | 50 ml | 12 €/l | 0,60 € |
| Sal y especias | global | - | 0,08 € |
| Guarnición (patata, verdura) | global | - | 0,55 € |
| **Total coste** | | | **4,29 €** |

```
Precio de venta: 18,50 €
Food cost: 4,29 / 18,50 × 100 = 23,2%
Margen bruto: 18,50 - 4,29 = 14,21 €
```

---

## 2. Gestión de mermas

### 2.1 Tipos de merma

| Tipo | Descripción | ¿Controlable? |
|---|---|---|
| **Merma de producción** | Pérdida durante cocinado (agua evaporada, huesos, pieles) | Parcialmente |
| **Merma de corte** | Pérdida al limpiar y cortar materias primas | Sí |
| **Merma de almacenamiento** | Deterioro por caducidad o mal almacenamiento | Sí |
| **Merma de servicio** | Pérdida por errores en comanda o devoluciones | Sí |
| **Merma involuntaria** | Robo, derrames, excesos en raciones | Sí |

### 2.2 Cálculo de la merma

```
Merma (%) = (Peso bruto - Peso neto) / Peso bruto × 100
```

Ejemplo: compras 5 kg de solomillo de cerdo. Tras limpiar y cortar, obtienes 3,8 kg utilizable.

```
Merma = (5 - 3,8) / 5 × 100 = 24%
```

**La merma real impacta directamente en tu food cost.** Si no la contabilizas, estás subestimando el coste real de tus platos.

### 2.3 Mermas objetivo por categoría

| Categoría | Merma media | Merma aceptable | Señal de alerta |
|---|---|---|---|
| Carne de vacuno | 20-28% | < 30% | > 35% |
| Carne de cerdo | 18-25% | < 28% | > 32% |
| Pollo entero | 25-32% | < 35% | > 40% |
| Pescado blanco | 15-22% | < 25% | > 30% |
| Pescado azul | 12-18% | < 22% | > 28% |
| Verduras y hortalizas | 20-35% | < 38% | > 45% |
| Fruta | 15-25% | < 28% | > 35% |

### 2.4 Estrategias para reducir mermas

1. **Buy whole and process in-house**: cheaper than pre-cut and less waste.
2. **Standardize cuts**: train the team to cut to exact specifications.
3. **Use trimmings**: make stocks, sauces, or side dishes from trimmings.
4. **Implement FIFO rigorously**: first in, first out rotation.
5. **Daily specials**: use approaching-expiry products in daily specials.
6. **Portion control**: weigh every portion during service.
7. **Track waste**: register every thrown-away item with reason.

---

## 3. Inventario y conteo físico

### 3.1 Tipos de inventario

#### Inventario perpetuo

Registro continuo de entradas y salidas. Ideal para productos de alto valor (carnes premium, pescado de alta gama).

```
Existencias actuales = Existencias iniciales + Entradas - Salidas
```

#### Inventario periódico

Conteo físico en fechas determinadas (semanal o quincenal). Más simple pero menos preciso.

#### Inventario cíclico (cycle counting)

Conteo parcial pero frecuente de categorías específicas. Divide el almacén en zonas y cuenta una zona diferente cada día.

### 3.2 Proceso de inventario valorado

1. **Prepara el inventario**: organiza productos por categoría.
2. **Cuenta físicamente**: número de unidades o peso de cada producto.
3. **Registra precios**: usa el último precio de compra o precio medio ponderado.
4. **Calcula el valor**: cantidad × precio unitario.
5. **Compara con el sistema**: identifica desviaciones y analízalas.

### 3.3 Plantilla de inventario

La plantilla de Excel disponible en [assets/templates/](../assets/templates/) incluye:

- Hoja de registro con categorías predefinidas.
- Cálculo automático de valor de existencias.
- Comparativa semanal con desviaciones en porcentaje y euros.
- Gráficos de tendencia por categoría.

---

## 4. Ingeniería de menú

### 4.1 Clasificación ABC de productos

Clasifica tus platos según el **análisis ABC** basado en dos dimensiones: margen de contribución y volumen de ventas.

#### Matriz de priorización

| | Alto margen | Bajo margen |
|---|---|---|
| **Alta venta** | **A) Platos estrellas**: prioriza visualmente, emplatado atractivo, formación del equipo | **B) Platos caballo de batalla**: necesarios para tráfico, considera optimización |
| **Baja venta** | **C) Platos潜在**： alto potencial si se promocionan, testear precio | **D) Platos problemáticos**: revisar o eliminar |

#### Acciones por clasificación

**Clase A (Estrellas):**

- Posición destacada en la carta (inicio, recuadro, con foto).
- Formación completa del equipo sobre estos platos.
- Calidad y emplatado impecables.
- Precios ligeramente más altos (test de sensibilidad).

**Clase B (Caballos de batalla):**

- Mantener si generan tráfico o complementan la carta.
- Buscar formas de mejorar su rentabilidad (reducir porción, cambiar ingrediente).
- Evaluar si el coste de mantenerlos justifica el margen que generan.

**Clase C (Incógnitas):**

- Promocionar activamente durante 2-4 semanas.
- Medir respuesta de ventas.
- Si la venta mejora, pasan a Clase A. Si no, eliminar.

**Clase D (Problemas):**

- Eliminar de la carta o reformular.
- Analizar si algún ingrediente puede reutilizarse.

### 4.2 Diseño de carta (menu engineering)

#### Principios de colocación

- **Gold zone**: esquina superior derecha de la carta (primer punto de atención en lectura occidental).
- **Anchor price**: el segundo plato más caro crea la percepción de que los demás son más baratos.
- **Decoy effect**: introduce un plato a precio muy alto para que el inmediatamente inferior parezca razonable.
- **Boxed items**: recuadrar platos destacados (platos del chef, especialidad de la casa) genera +15-20% de ventas.

#### Longitud de la carta

- **Platos principales**: 8-12 opciones (óptimo). Más de 15 genera parálisis de decisión.
- **Entrantes**: 4-6 opciones.
- **Postres**: 4-6 opciones.
- Menos es más: una carta concisa reduce costes de inventario y mejora la percepción de calidad.

---

## 5. Sistemas de costeo avanzada

### 5.1 Costeo basado en actividad (ABC costing)

Para restaurantes complejos, el ABC costing asigna costes indirectos a cada plato proporcionalmente al uso que hacen de los recursos.

```
Coste total del plato = Coste directo + (Coste indirecto × conductor de actividad)
```

Ejemplo de conductor de actividad:

- Tiempo de horno: 1 plato en horno 15 min = 15 min × coste por minuto de horno.
- Tiempo de chef: 1 plato requiere 8 min de chef = 8 min × coste por minuto de chef.
- Espacio en cámara: 1 plato ocupa 0,5 horas de cámara = 0,5 × coste por hora de almacenamiento.

### 5.2 Costeo objetivo (Target costing)

A la inversa: empiezas por el precio de mercado,restas tu margen objetivo y obtienes el coste máximo admissible.

```
Coste objetivo = Precio de mercado - Margen objetivo
```

Si el mercado cobra 16 € por un plato similar y tu margen objetivo es 70%, tu coste máximo es:

```
Coste objetivo = 16 × (1 - 0,70) = 4,80 €
```

Si tu receta actual cuesta 5,20 €, necesitas reducir 0,40 € de coste (reformular, cambiar ingrediente, ajustar porción).

---

## 6. Herramientas de monitorización

### 6.1 Tablero de control semanal

| Métrica | Definición | Frecuencia | Fuente |
|---|---|---|---|
| Food cost total | (Inventario inicial + Compras - Inventario final) / Ventas | Semanal | Inventario + TPV |
| Food cost por categoría | Coste de cada categoría / Ventas de esa categoría | Semanal | Inventario por categoría |
| Merma global | Merma total / Total compras | Semanal | Registro de mermas |
| Desviación de precio | Precio real vs. precio teóricode plato | Mensual | Ticket promedio |
| Ocupación media | Cubiertos / Capacidad máxima | Semanal | TPV |
| Ticket medio | Ventas / Número de cubiertos | Semanal | TPV |

### 6.2 Alertas y acciones

| Señal | Umbral | Acción |
|---|---|---|
| Food cost > objetivo + 2 puntos | > 32% (objetivo 30%) | Revisar receta, porción, merma o robo |
| Merma > 7% | > 7% | Investigación profunda, formación |
| Ticket medio < objetivo | < 90% del objetivo | Revisar carta, formación en ventas |
| Desviación inventario > 3% | > 3% | Auditoría de recetas, control de acceso |
| Ocupación < 50% durante 2 semanas | < 50% | Activar promociones, revisar propuesta |

---

## 7. Prevención de pérdidas (shrinkage)

El **shrinkage** en restauración incluye:merma, errores en recetas, devoluciones, robos y derrames.

### 7.1 Principales causas de pérdida

1. **Robo de empleados**: estimado entre 1-3% de las ventas en la industria.
2. **Robo de proveedores**: manipulación de albaranes, entregas cortas.
3. **Errores de porción**: raciones mayores de lo estándar.
4. **Devoluciones no registradas**: platos devueltos que no se restan del coste.
5. **Mal almacenamiento**: productos caducados o deteriorados.
6. **Sobreproducción**: producir más de lo que se vende.

### 7.2 Controles internos

- **Separación de funciones**: quien pide no recibe, quien recibe no almacena, quien almacena no cocina.
- **Conciliación diaria**: ventas TPV vs. cash en caja vs. consumo teórico.
- **Acceso restringido**: solo personal autorizado a almacén y zona de expedición.
- **Cámaras de seguridad**: en zonas de caja, almacén y entrada de mercancía.
- **Inventarios sorpresa**: al menos 1 al mes sin previo aviso.

---

*Para profundizar en la aplicación práctica de estos sistemas, consulta el [manual de Finanzas básicas](../manuales/finanzas-basicas.md). Para una personalización completa de tu sistema de control de costes, contacta a través de [david@example.com](mailto:david@example.com).*
