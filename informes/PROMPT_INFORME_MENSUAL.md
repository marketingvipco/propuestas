# PROMPT ESTÁNDAR — INFORME MENSUAL MARKETING VIP®
> Guardar este archivo. Usarlo cada mes para generar informes de cualquier cliente.

---

## CÓMO USARLO

Copia y pega este prompt en Claude al inicio de cada mes:

---

## EL PROMPT

```
Genera el informe mensual de gestión para el cliente [NOMBRE DEL CLIENTE].

**Datos del cliente:**
- Nombre: [NOMBRE]
- Mes a reportar: [MES] [AÑO]
- ClickUp List ID: [ID_LISTA]
- Instagram Business Account ID: [IG_ID]
- Facebook Page ID: [PAGE_ID]
- Meta Ads Account ID: [act_XXXXXXXXXX]
- Brevo API Key: [xkeysib-...]  ← opcional, agregar cuando esté disponible
- URL del informe anterior (para comparativa): [URL_MES_ANTERIOR]  ← opcional

**Instrucciones:**
Sigue el formato estándar de Marketing VIP® exactamente como está en:
https://marketingvipco.github.io/propuestas/informes/arichy-real-estate-marzo-2026.html

Genera el informe completo con:
1. Hero portada con nombre del cliente
2. Resumen ejecutivo con KPIs (estilo Reportei: valor + variación vs mes anterior)
3. Sección Instagram orgánico vía IG API (con tabla de posts + thumbnails reales + métricas)
4. Sección Meta Ads vía API (campañas, acciones, comparativa orgánico vs pagado)
5. Sección Mail Marketing — Brevo (si hay API key disponible)
6. Sección ClickUp — tareas gestionadas en el mes (contenido publicado, estratégicas, correcciones)
7. Comparativa mes anterior vs mes actual (si hay URL anterior)
8. Próximos pasos por área

Publica en: https://marketingvipco.github.io/propuestas/informes/[slug-cliente]-[mes]-[año].html

REGLAS DE DISEÑO (NUNCA CAMBIAR):
- Misma estructura HTML/CSS del informe de referencia
- Fuente: Geist (Google Fonts)
- Colores: --navy #1A1A2E · --green #51DD7D
- Hero oscuro con grid decorativo
- Secciones alternas blanco / gris claro
- Badges de color por formato (Reel morado, Carrusel azul, Historia ámbar, Post verde)
- Pills de estado por color (Publicado verde, Stand By amarillo, En Cambios rojo, etc.)
- KPI cards navy con valor + label + línea de variación vs mes anterior
- Tablas con thead navy, filas alternadas blanco/gris
- analysis-block con borde izquierdo verde (orgánico) o azul (Meta Ads) o rosa (IG)
- Thumbnails reales de IG API en la tabla de posts (48x48px, click → Instagram)
- Footer: "© [AÑO] Marketing VIP® · Datos: Meta Graph API v19.0 · Instagram Graph API · ClickUp API"
```

---

## DATOS DE CLIENTES CONFIGURADOS

### Arichy Real Estate
| Campo | Valor |
|-------|-------|
| ClickUp List ID | `901324565657` |
| Instagram ID | `17841454974456376` |
| Facebook Page ID | `976877848844666` |
| Meta Ads Account | `act_255327741430906​10` |
| Token Meta | *(renovar mensualmente en Business Manager → Usuarios del sistema)* |
| Brevo API Key | *(pendiente)* |
| Slug | `arichy-real-estate` |

### Euro Money Exchange
| Campo | Valor |
|-------|-------|
| ClickUp List ID | `901324303147` |
| Instagram ID | *(pendiente)* |
| Meta Ads Account | *(pendiente)* |
| Slug | `euro-money` |

### Miami Money Exchange
| Campo | Valor |
|-------|-------|
| ClickUp List ID | `901324303203` |
| Instagram ID | *(pendiente)* |
| Meta Ads Account | *(pendiente)* |
| Slug | `miami-money` |

### AC Depot
| Campo | Valor |
|-------|-------|
| ClickUp List ID | `901322350882` |
| Instagram ID | *(pendiente)* |
| Meta Ads Account | *(pendiente)* |
| Slug | `ac-depot` |

---

## SCRIPTS DISPONIBLES (en /scripts/)

| Script | Qué hace |
|--------|----------|
| `meta-fetch.js` | Jala campañas + métricas de Meta Ads API |
| `organic-fetch.js` | Jala posts + métricas de Instagram Graph API |
| `compare-fetch.js` | Jala datos de 2 meses para comparativa |
| `media-thumbs.js` | Jala thumbnails reales de cada post de IG |

**Uso:**
```bash
node scripts/meta-fetch.js 2026-04-01 2026-04-30
node scripts/organic-fetch.js 2026-04-01 2026-04-30
node scripts/compare-fetch.js  # compara mes anterior vs actual automáticamente
```

---

## CHECKLIST MENSUAL

Antes de pedir el informe, verificar:
- [ ] Token Meta Ads vigente (duran ~60 días con System User, o renovar en Explorador API)
- [ ] ClickUp List ID correcto para el cliente
- [ ] Instagram Business Account ID del cliente
- [ ] Meta Ads Account ID (`act_XXXXXXXXXX`)
- [ ] URL del informe del mes anterior para comparativa
- [ ] Brevo API Key (cuando esté disponible)

---

## ESTRUCTURA DE URLs

```
https://marketingvipco.github.io/propuestas/informes/[slug]-[mes]-[año].html
```

Ejemplos:
- `arichy-real-estate-marzo-2026.html`
- `euro-money-abril-2026.html`
- `miami-money-abril-2026.html`
- `ac-depot-abril-2026.html`

---

## NOTA SOBRE EL TOKEN META

El token actual (`EAAbG6Y0Tti...`) es un token de usuario de corta duración.
Para producción, generar un **System User Token** permanente:
1. Business Manager → Configuración → Usuarios del sistema
2. Crear usuario → Administrador
3. Asignar cuentas publicitarias
4. Generar token → permisos: `ads_read`, `business_management`, `read_insights`
5. Este token no expira

---

*Documento creado por Marketing VIP® · Última actualización: Abril 2026*
