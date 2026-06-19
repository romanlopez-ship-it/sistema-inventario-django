# Sprint 1 Review — Sistema de Inventario
## Fecha: ___________

### Sprint Goal verificado
"El sistema muestra la lista de productos y el detalle de cada uno
 accesible por URL, con plantillas HTML separadas del código Python."

### Incremento entregado
- ✅ Vista `lista_productos` con plantilla `lista.html`
- ✅ Vista `detalle_producto` con plantilla `detalle.html`
- ✅ Herencia de `base.html` (header/footer compartidos)
- ✅ Status 404 para productos inexistentes

### Criterios de aceptación verificados (Gherkin)
HU-01: Ver lista de productos
  ✅ Dado 3 productos / Cuando GET /productos/ / Entonces lista con nombres y enlaces

HU-01a: Ver detalle de producto
  ✅ Dado ID=1 / Cuando GET /productos/1/ / Entonces nombre y precio correctos
  ✅ Dado ID=99 / Cuando GET /productos/99/ / Entonces status 404

### Deuda técnica identificada
- Los datos son estáticos (diccionario). Sprint 2 introducirá la base de datos.

### Sprint 2 — Historia seleccionada
HU-02: Registrar un producto nuevo (requiere modelo + formulario — Semana 4)