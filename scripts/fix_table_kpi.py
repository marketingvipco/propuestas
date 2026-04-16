f = open(r'C:\Users\adria\propuestas-mvip\informes\arichy-real-estate-marzo-2026.html', encoding='utf-8')
c = f.read()
f.close()

# ── FIX 1: tag roto en la fila del Día de la Mujer ──────────────────────────
c = c.replace('<tdclass="td-bold">66</td>', '<td class="td-bold">66</td>')

# ── FIX 2: KPI cards con estilo Reportei (val + variación + periodo anterior)
# Reemplazar el bloque de KPIs del resumen ejecutivo
old_kpi_resumen = '''    <div class="kpi-grid kpi-grid-6">
      <div class="kpi-card"><div class="kpi-val">12</div><div class="kpi-lbl">Posts publicados IG</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">1,889</div><div class="kpi-lbl">Seguidores totales</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">2,933</div><div class="kpi-lbl">Alcance orgánico total</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">66</div><div class="kpi-lbl">Likes máx. (Día Mujer)</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">$112</div><div class="kpi-lbl">Gasto Meta Ads</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">126K</div><div class="kpi-lbl">Impresiones pagadas</div></div>
    </div>'''

new_kpi_resumen = '''    <div class="kpi-grid kpi-grid-6">
      <div class="kpi-card"><div class="kpi-val">12</div><div class="kpi-lbl">Posts publicados IG</div><div class="kpi-vs"><span class="kpi-delta up">▲ +71%</span> vs 7 en Feb</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">1,889</div><div class="kpi-lbl">Seguidores totales</div><div class="kpi-vs">Perfil activo · 551 posts</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">2,933</div><div class="kpi-lbl">Alcance orgánico</div><div class="kpi-vs"><span class="kpi-delta up">▲ +96%</span> vs 1,499 en Feb</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">151</div><div class="kpi-lbl">Likes totales</div><div class="kpi-vs"><span class="kpi-delta up">▲ +47%</span> vs 103 en Feb</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">$112.13</div><div class="kpi-lbl">Gasto Meta Ads</div><div class="kpi-vs">Camp. activa desde 17 Mar</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">126,290</div><div class="kpi-lbl">Impresiones pagadas</div><div class="kpi-vs"><span class="kpi-delta up">▲ Nuevo</span> CPC $0.042</div></div>
    </div>'''

c = c.replace(old_kpi_resumen, new_kpi_resumen)

# ── FIX 3: KPI cards IG section también con variación ──────────────────────
old_kpi_ig = '''    <div class="kpi-grid kpi-grid-5">
      <div class="kpi-card ig-card"><div class="kpi-val">1,889</div><div class="kpi-lbl">Seguidores actuales</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">551</div><div class="kpi-lbl">Posts totales en perfil</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">12</div><div class="kpi-lbl">Posts en marzo</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">2,933</div><div class="kpi-lbl">Alcance orgánico total</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">71</div><div class="kpi-lbl">Shares totales</div></div>
    </div>'''

new_kpi_ig = '''    <div class="kpi-grid kpi-grid-5">
      <div class="kpi-card ig-card"><div class="kpi-val">1,889</div><div class="kpi-lbl">Seguidores actuales</div><div class="kpi-vs">@arichyrealestate</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">2,933</div><div class="kpi-lbl">Alcance orgánico</div><div class="kpi-vs"><span class="kpi-delta up">▲ +95.7%</span> vs Feb</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">151</div><div class="kpi-lbl">Likes totales</div><div class="kpi-vs"><span class="kpi-delta up">▲ +46.6%</span> vs Feb</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">71</div><div class="kpi-lbl">Shares totales</div><div class="kpi-vs"><span class="kpi-delta up">▲ +39.2%</span> vs Feb</div></div>
      <div class="kpi-card ig-card"><div class="kpi-val">244</div><div class="kpi-lbl">Alcance / post</div><div class="kpi-vs"><span class="kpi-delta up">▲ +14%</span> vs 214 Feb</div></div>
    </div>'''

c = c.replace(old_kpi_ig, new_kpi_ig)

# ── FIX 4: Meta KPI cards con variación ────────────────────────────────────
old_kpi_meta = '''    <div class="kpi-grid kpi-grid-6">
      <div class="kpi-card meta-card"><div class="kpi-val">$112.13</div><div class="kpi-lbl">Gasto total (USD)</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">126,290</div><div class="kpi-lbl">Impresiones</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">70,904</div><div class="kpi-lbl">Alcance pagado</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">2,675</div><div class="kpi-lbl">Clicks totales</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">$0.042</div><div class="kpi-lbl">CPC (USD)</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">6,707</div><div class="kpi-lbl">Video views</div></div>
    </div>'''

new_kpi_meta = '''    <div class="kpi-grid kpi-grid-6">
      <div class="kpi-card meta-card"><div class="kpi-val">$112.13</div><div class="kpi-lbl">Gasto total (USD)</div><div class="kpi-vs">Camp. iniciada 17 Mar</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">126,290</div><div class="kpi-lbl">Impresiones</div><div class="kpi-vs">Frecuencia 1.78x</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">70,904</div><div class="kpi-lbl">Alcance pagado</div><div class="kpi-vs">CPM $0.89 USD</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">2,675</div><div class="kpi-lbl">Clicks totales</div><div class="kpi-vs">2,574 link clicks</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">$0.042</div><div class="kpi-lbl">CPC (USD)</div><div class="kpi-vs"><span class="kpi-delta up">▼ 97%</span> bajo benchmark</div></div>
      <div class="kpi-card meta-card"><div class="kpi-val">6,707</div><div class="kpi-lbl">Video views</div><div class="kpi-vs">$0.017 por reproducción</div></div>
    </div>'''

c = c.replace(old_kpi_meta, new_kpi_meta)

# ── FIX 5: Agregar CSS para .kpi-vs y .kpi-delta dentro del bloque de estilos existente
new_css = """
/* kpi variaciones estilo reportei */
.kpi-vs{font-size:11px;color:rgba(255,255,255,.4);margin-top:6px;line-height:1.3;}
.kpi-delta{font-weight:700;font-size:11px;}
.kpi-delta.up{color:#86EFAC;}
.kpi-delta.down{color:#FCA5A5;}
"""
c = c.replace('/* thumbnails tabla */', new_css + '\n/* thumbnails tabla */')

open(r'C:\Users\adria\propuestas-mvip\informes\arichy-real-estate-marzo-2026.html', 'w', encoding='utf-8').write(c)
print('ok', len(c))
