import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="Samsung Social Trends | Executive Insights",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ESTILO E PALETA DE CORES (Samsung Corporate Identity)
COLORS = {
    'primary': '#034EA2',    # Azul Samsung
    'secondary': '#000000',  # Preto
    'accent': '#1428a0',     # Azul Royal
    'background': '#F8F9FA', # Cinza muito claro
    'card': '#FFFFFF',       # Branco
    'text': '#333333'
}

def apply_custom_styles():
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
        .main {{ background-color: {COLORS['background']}; font-family: 'Inter', sans-serif; }}
        
        /* Estilização de KPI Cards */
        .kpi-box {{
            background: white;
            padding: 20px;
            border-radius: 12px;
            border-top: 4px solid {COLORS['primary']};
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            text-align: center;
        }}
        .kpi-value {{ font-size: 1.8rem; font-weight: bold; color: {COLORS['primary']}; margin: 5px 0; }}
        .kpi-label {{ font-size: 0.8rem; color: #666; text-transform: uppercase; letter-spacing: 1px; }}
        
        /* Influencer Cards */
        .influencer-card {{
            background: white;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 15px;
            border: 1px solid #E0E0E0;
            transition: 0.3s ease;
        }}
        .influencer-card:hover {{
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            transform: translateY(-3px);
            border-color: {COLORS['primary']};
        }}
        
        /* Botão de Link */
        .btn-link {{
            text-decoration: none;
            color: white !important;
            background: {COLORS['primary']};
            padding: 8px 20px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: bold;
            display: inline-block;
        }}
        </style>
    """, unsafe_allow_html=True)

# 3. CARREGAMENTO E LIMPEZA DE DADOS
@st.cache_data
def load_data():
    try:
        df = pd.read_excel('Samsung_base_reclassificada_COM_descricao.xlsx')
        numeric_cols = ['engajamento', 'followers', 'audienceSizes', 'socialPowers', 
                        'mediaPowers', 'likes', 'shares', 'comentarios']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return pd.DataFrame()

def format_num(num):
    if num >= 1_000_000: return f"{num/1_000_000:.1f}M"
    if num >= 1_000: return f"{num/1_000:.1f}K"
    return f"{int(num)}"

# --- INÍCIO DO APP ---
df = load_data()
apply_custom_styles()

# Remover categoria "Outros/Sem Categoria" e valores vazios
if not df.empty:
    df = df[df['MacroTrends'] != 'Outros/Sem Categoria']
    df = df[df['MacroTrends'].notna()]  # Remover valores NaN

if not df.empty:
    # Sidebar
    st.sidebar.title("Trends Dashboard")
    page = st.sidebar.radio("Navegação", ["Macro & Micro Trends", "Microtrends & Influencers"])

    # --- PÁGINA 1: MACRO & MICRO TRENDS ---
    if page == "Macro & Micro Trends":
        st.title("Insights de Tendências")
        
        # Filtros na Sidebar (responsivos em cascata)
        st.sidebar.markdown("---")
        
        # Criar dicionário de descrições para MacroTrends
        macro_descricoes_p1 = {}
        if 'Descricao Macrotrends' in df.columns:
            for macro in df['MacroTrends'].dropna().unique():
                desc = df[df['MacroTrends'] == macro]['Descricao Macrotrends'].iloc[0]
                if pd.notna(desc) and str(desc) != 'nan':
                    macro_descricoes_p1[macro] = desc
        
        # 1. Filtro de MacroTrend
        f_macro_p1 = st.sidebar.multiselect(
            "Filtrar MacroTrend", 
            options=df['MacroTrends'].unique(), 
            default=df['MacroTrends'].unique(),
            key='p1_macro'
        )
        
        # Mostrar descrições das MacroTrends SELECIONADAS
        if f_macro_p1 and len(f_macro_p1) < len(df['MacroTrends'].unique()):
            for macro in f_macro_p1:
                if macro in macro_descricoes_p1:
                    st.sidebar.markdown(f"""
                        <div style="background: #f0f2f6; padding: 8px; border-radius: 5px; margin-bottom: 8px; font-size: 0.8rem;">
                            <div style="font-weight: 600; color: #034EA2; margin-bottom: 4px;">📌 {macro}</div>
                            <div style="color: #555; line-height: 1.3;">{macro_descricoes_p1[macro]}</div>
                        </div>
                    """, unsafe_allow_html=True)
        
        # Aplicar filtro de MacroTrend
        df_filtered_p1 = df[df['MacroTrends'].isin(f_macro_p1)]
        
        # Criar dicionário de descrições para MicroTrends (filtrado)
        micro_descricoes_p1 = {}
        if 'Descricao Microtrends' in df.columns:
            for micro in df_filtered_p1['MicroTrends'].dropna().unique():
                desc = df_filtered_p1[df_filtered_p1['MicroTrends'] == micro]['Descricao Microtrends'].iloc[0]
                if pd.notna(desc) and str(desc) != 'nan':
                    micro_descricoes_p1[micro] = desc
        
        # 2. Filtro de MicroTrend (responsivo a MacroTrend)
        f_micro_p1 = st.sidebar.multiselect(
            "Filtrar MicroTrend", 
            options=df_filtered_p1['MicroTrends'].unique(), 
            default=df_filtered_p1['MicroTrends'].unique(),
            key='p1_micro'
        )
        
        # Mostrar descrições das MicroTrends SELECIONADAS
        if f_micro_p1 and len(f_micro_p1) < len(df_filtered_p1['MicroTrends'].unique()):
            for micro in f_micro_p1:
                if micro in micro_descricoes_p1:
                    st.sidebar.markdown(f"""
                        <div style="background: #f0f2f6; padding: 8px; border-radius: 5px; margin-bottom: 8px; font-size: 0.8rem;">
                            <div style="font-weight: 600; color: #034EA2; margin-bottom: 4px;">📌 {micro}</div>
                            <div style="color: #555; line-height: 1.3;">{micro_descricoes_p1[micro]}</div>
                        </div>
                    """, unsafe_allow_html=True)
        
        # Aplicação final dos filtros
        dff = df_filtered_p1[df_filtered_p1['MicroTrends'].isin(f_micro_p1)]

        # 1. Tree Map Reativo
        st.subheader("Distribuição: Macrotrends por Engajamento (Views)")
        macro_plot = dff.groupby('MacroTrends')['engajamento'].sum().reset_index()
        
        # Quebra de texto para caber nas caixas
        def quebrar_texto(texto, max_chars=20):
            palavras = str(texto).split()
            linhas = []
            linha_atual = []
            tam_atual = 0
            
            for palavra in palavras:
                if tam_atual + len(palavra) + 1 <= max_chars:
                    linha_atual.append(palavra)
                    tam_atual += len(palavra) + 1
                else:
                    if linha_atual:
                        linhas.append(' '.join(linha_atual))
                    linha_atual = [palavra]
                    tam_atual = len(palavra)
            
            if linha_atual:
                linhas.append(' '.join(linha_atual))
            
            return '<br>'.join(linhas)
        
        # Adicionar engajamento em MM ao label
        def criar_label_com_engajamento(row):
            texto_quebrado = quebrar_texto(row['MacroTrends'])
            engajamento_mm = f"({row['engajamento']/1_000_000:.1f}MM)"
            return f"{texto_quebrado}<br>{engajamento_mm}"
        
        macro_plot['MacroTrends_Quebrado'] = macro_plot.apply(criar_label_com_engajamento, axis=1)
        
        fig_tree = px.treemap(macro_plot, path=['MacroTrends_Quebrado'], values='engajamento',
                              color='engajamento', color_continuous_scale='Blues')
        fig_tree.update_traces(
            textfont=dict(size=13, family='Inter', color='black'),
            textposition='middle center',
            marker=dict(line=dict(width=2, color='white'))
        )
        fig_tree.update_layout(
            height=700,
            uniformtext=dict(minsize=8, mode='show')
        )
        st.plotly_chart(fig_tree, use_container_width=True)

        # 1.5. Lista de MacroTrends com Descrições
        st.subheader("Macrotrends Identificadas")
        
        # Obter MacroTrends únicas e suas descrições
        if 'Descricao Macrotrends' in dff.columns:
            macros_info = dff.groupby('MacroTrends').agg({
                'Descricao Macrotrends': 'first',
                'engajamento': 'sum'
            }).sort_values('engajamento', ascending=False).reset_index()
        else:
            macros_info = dff.groupby('MacroTrends').agg({
                'engajamento': 'sum'
            }).sort_values('engajamento', ascending=False).reset_index()
            macros_info['Descricao Macrotrends'] = 'Descrição não disponível'
        
        # Criar cards para cada MacroTrend
        for idx, row in macros_info.iterrows():
            descricao = str(row.get('Descricao Macrotrends', 'Descrição não disponível'))
            if pd.isna(descricao) or descricao == 'nan':
                descricao = 'Descrição não disponível'
            
            st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
                    border-left: 5px solid {COLORS['primary']};
                    border-radius: 10px;
                    padding: 12px 18px;
                    margin-bottom: 12px;
                    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
                    transition: all 0.3s ease;
                ">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <h4 style="color: {COLORS['primary']}; margin: 0; font-size: 1.1rem; font-weight: 700;">
                            {row['MacroTrends']}
                        </h4>
                        <span style="
                            background: {COLORS['primary']};
                            color: white;
                            padding: 5px 14px;
                            border-radius: 20px;
                            font-size: 0.8rem;
                            font-weight: 600;
                        ">
                            {format_num(row['engajamento'])} views
                        </span>
                    </div>
                    <p style="
                        color: #555;
                        margin: 0;
                        line-height: 1.5;
                        font-size: 0.9rem;
                    ">
                        {descricao}
                    </p>
                </div>
            """, unsafe_allow_html=True)

        # 2. Campo de Texto Dinâmico
        st.markdown(f"""
            <div style="background:#034EA2; color:white; padding:20px; border-radius:12px; margin-bottom:25px;">
                <b>Análise Ativa:</b> Exibindo dados de {len(dff['MacroTrends'].unique())} Macrotrends 
                e {len(dff['MicroTrends'].unique())} Microtrends baseadas na sua seleção.
            </div>
        """, unsafe_allow_html=True)

        # 3. Bar Chart Reativo com Descrições
        st.subheader("Top Microtrends por Visualizações")
        
        # Obter MicroTrends com descrições
        if 'Descricao Microtrends' in dff.columns:
            micro_plot = dff.groupby('MicroTrends').agg({
                'engajamento': 'sum',
                'Descricao Microtrends': 'first'
            }).sort_values('engajamento', ascending=False).head(15).reset_index()
        else:
            micro_plot = dff.groupby('MicroTrends')['engajamento'].sum().sort_values(ascending=False).head(15).reset_index()
            micro_plot['Descricao Microtrends'] = 'Descrição não disponível'
        
        # Tratar descrições vazias
        micro_plot['Descricao Microtrends'] = micro_plot['Descricao Microtrends'].apply(
            lambda x: x if pd.notna(x) and str(x) != 'nan' else 'Descrição não disponível'
        )
        
        fig_bar = px.bar(micro_plot, x='engajamento', y='MicroTrends', orientation='h',
                         color='engajamento', color_continuous_scale='GnBu',
                         custom_data=['Descricao Microtrends'])
        
        fig_bar.update_traces(
            hovertemplate='<b>%{y}</b><br>' +
                         'Engajamento: %{x:,.0f}<br>' +
                         '<i>%{customdata[0]}</i><br>' +
                         '<extra></extra>'
        )
        
        fig_bar.update_layout(
            yaxis={'categoryorder':'total ascending'}, 
            showlegend=False,
            height=600,
            hoverlabel=dict(
                bgcolor="white",
                font_size=13,
                font_family="Inter"
            )
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # --- PÁGINA 2: MICROTRENDS & INFLUENCERS ---
    else:
        st.title("Detalhamento de Influenciadores")
        
        # Filtros na Sidebar (responsivos em cascata)
        st.sidebar.markdown("---")
        
        # 1. Filtro de Canal
        f_origem = st.sidebar.multiselect("Filtrar Canal", options=df['origem'].unique(), default=df['origem'].unique())
        
        # Aplicar filtro de Canal
        df_filtered_origem = df[df['origem'].isin(f_origem)]
        
        # Criar dicionário de descrições para MacroTrends
        macro_descricoes = {}
        if 'Descricao Macrotrends' in df.columns:
            for macro in df_filtered_origem['MacroTrends'].dropna().unique():
                desc = df_filtered_origem[df_filtered_origem['MacroTrends'] == macro]['Descricao Macrotrends'].iloc[0]
                if pd.notna(desc) and str(desc) != 'nan':
                    macro_descricoes[macro] = desc
        
        # 2. Filtro de MacroTrend (responsivo a Canal)
        f_macro = st.sidebar.multiselect(
            "Filtrar MacroTrend", 
            options=df_filtered_origem['MacroTrends'].unique(), 
            default=df_filtered_origem['MacroTrends'].unique()
        )
        
        # Mostrar descrições das MacroTrends SELECIONADAS
        if f_macro and len(f_macro) < len(df_filtered_origem['MacroTrends'].unique()):
            for macro in f_macro:
                if macro in macro_descricoes:
                    st.sidebar.markdown(f"""
                        <div style="background: #f0f2f6; padding: 8px; border-radius: 5px; margin-bottom: 8px; font-size: 0.8rem;">
                            <div style="font-weight: 600; color: #034EA2; margin-bottom: 4px;">📌 {macro}</div>
                            <div style="color: #555; line-height: 1.3;">{macro_descricoes[macro]}</div>
                        </div>
                    """, unsafe_allow_html=True)
        
        # Aplicar filtros de Canal + MacroTrend
        df_filtered_macro = df_filtered_origem[df_filtered_origem['MacroTrends'].isin(f_macro)]
        
        # Criar dicionário de descrições para MicroTrends (filtrado)
        micro_descricoes = {}
        if 'Descricao Microtrends' in df.columns:
            for micro in df_filtered_macro['MicroTrends'].dropna().unique():
                desc = df_filtered_macro[df_filtered_macro['MicroTrends'] == micro]['Descricao Microtrends'].iloc[0]
                if pd.notna(desc) and str(desc) != 'nan':
                    micro_descricoes[micro] = desc
        
        # 3. Filtro de MicroTrend (responsivo a Canal + MacroTrend)
        f_micro = st.sidebar.multiselect(
            "Filtrar MicroTrend", 
            options=df_filtered_macro['MicroTrends'].unique(), 
            default=df_filtered_macro['MicroTrends'].unique()
        )
        
        # Mostrar descrições das MicroTrends SELECIONADAS
        if f_micro and len(f_micro) < len(df_filtered_macro['MicroTrends'].unique()):
            for micro in f_micro:
                if micro in micro_descricoes:
                    st.sidebar.markdown(f"""
                        <div style="background: #f0f2f6; padding: 8px; border-radius: 5px; margin-bottom: 8px; font-size: 0.8rem;">
                            <div style="font-weight: 600; color: #034EA2; margin-bottom: 4px;">📌 {micro}</div>
                            <div style="color: #555; line-height: 1.3;">{micro_descricoes[micro]}</div>
                        </div>
                    """, unsafe_allow_html=True)
        
        # Aplicar filtros de Canal + MacroTrend + MicroTrend
        df_filtered = df_filtered_macro[df_filtered_macro['MicroTrends'].isin(f_micro)]
        
        # 4. Filtro de Influenciador (responsivo a todos os filtros acima)
        st.sidebar.markdown("---")
        influencers_disponiveis = sorted(df_filtered['nickName'].dropna().unique().tolist())
        f_influencer = st.sidebar.selectbox(
            "Filtrar Influenciador",
            options=["Todos"] + influencers_disponiveis,
            help="Digite para buscar um influenciador específico"
        )
        
        # Aplicação final de todos os filtros
        dff = df_filtered.copy()
        if f_influencer != "Todos":
            dff = dff[dff['nickName'] == f_influencer]

        # 1. Coluna de Indicadores (KPIs)
        k_cols = st.columns(6)
        k_metrics = [
            ("Vídeos", len(dff)),
            ("Views", dff['engajamento'].sum()),
            ("Followers", dff['followers'].sum()),
            ("Likes", dff['likes'].sum()),
            ("Shares", dff['shares'].sum()),
            ("Comments", dff['comentarios'].sum())
        ]
        
        for col, (label, val) in zip(k_cols, k_metrics):
            with col:
                st.markdown(f"""<div class="kpi-box"><div class="kpi-label">{label}</div><div class="kpi-value">{format_num(val)}</div></div>""", unsafe_allow_html=True)

        st.markdown("---")
        
        # 2. Gráfico de Frequência de Microtrends (Otimizado)
        st.subheader("Frequência de Microtrends")
        
        # Preparar dados com descrições e engajamento
        if 'Descricao Microtrends' in dff.columns:
            micro_freq = dff.groupby('MicroTrends').agg({
                'video_id': 'count',
                'engajamento': 'sum',
                'Descricao Microtrends': 'first'
            }).reset_index()
            micro_freq.columns = ['MicroTrends', 'count', 'engajamento', 'descricao']
        else:
            micro_freq = dff.groupby('MicroTrends').agg({
                'video_id': 'count',
                'engajamento': 'sum'
            }).reset_index()
            micro_freq.columns = ['MicroTrends', 'count', 'engajamento']
            micro_freq['descricao'] = 'Sem descrição'
        
        # Tratar descrições vazias
        micro_freq['descricao'] = micro_freq['descricao'].apply(
            lambda x: x if pd.notna(x) and str(x) != 'nan' else 'Sem descrição'
        )
        
        # Calcular percentual
        total_videos = micro_freq['count'].sum()
        micro_freq['percentual'] = (micro_freq['count'] / total_videos * 100).round(1)
        
        # Top 10
        micro_freq = micro_freq.nlargest(10, 'count')
        
        # Truncar labels longos para melhor visualização
        micro_freq['MicroTrends_Display'] = micro_freq['MicroTrends'].apply(
            lambda x: x[:40] + '...' if len(str(x)) > 40 else x
        )
        
        # Criar gráfico com tooltips ricos
        fig_f = px.bar(
            micro_freq, 
            x='count', 
            y='MicroTrends_Display', 
            orientation='h',
            color='count',
            color_continuous_scale='Purples',
            custom_data=['MicroTrends', 'descricao', 'engajamento', 'percentual']
        )
        
        # Configurar tooltip rico
        fig_f.update_traces(
            hovertemplate='<b>%{customdata[0]}</b><br><br>' +
                         '<i>%{customdata[1]}</i><br><br>' +
                         '📊 Vídeos: <b>%{x}</b> (%{customdata[3]}%)<br>' +
                         '👁️ Engajamento: <b>%{customdata[2]:,.0f}</b> views<br>' +
                         '<extra></extra>',
            texttemplate='%{x}',
            textposition='outside'
        )
        
        # Layout otimizado
        fig_f.update_layout(
            yaxis={'categoryorder': 'total ascending', 'title': None},
            xaxis={'title': 'Número de Vídeos'},
            showlegend=False,
            height=700,
            hoverlabel=dict(
                bgcolor="white",
                font_size=13,
                font_family="Inter"
            ),
            margin=dict(l=0, r=40, t=10, b=40)
        )
        
        st.plotly_chart(fig_f, use_container_width=True)
        
        # 3. Gráfico de Bolhas (Social vs Media Power)
        st.subheader("Social vs Media Power")
        
        # Legenda explicativa visual
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, {COLORS['background']} 0%, #ffffff 100%); border: 2px solid {COLORS['primary']}; border-radius: 12px; padding: 20px; margin-bottom: 20px;">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px;">
                    <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #9C27B0;">
                        <div style="display: flex; align-items: center; margin-bottom: 8px;">
                            <span style="font-size: 1.5rem; margin-right: 10px;">⭕</span>
                            <strong style="color: {COLORS['primary']}; font-size: 0.95rem;">Tamanho das Bolhas</strong>
                        </div>
                        <p style="margin: 0; font-size: 0.85rem; color: #555; line-height: 1.4;">
                            <strong>Audience Size:</strong> Número de seguidores do influenciador
                        </p>
                    </div>
                    <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #2196F3;">
                        <div style="display: flex; align-items: center; margin-bottom: 8px;">
                            <span style="font-size: 1.5rem; margin-right: 10px;">↔️</span>
                            <strong style="color: {COLORS['primary']}; font-size: 0.95rem;">Eixo Horizontal (X)</strong>
                        </div>
                        <p style="margin: 0; font-size: 0.85rem; color: #555; line-height: 1.4;">
                            <strong>Social Power:</strong> Mede interação e engajamento com seguidores. Identifica influenciadores populares em <em>nichos específicos</em>
                        </p>
                    </div>
                    <div style="background: white; padding: 12px; border-radius: 8px; border-left: 4px solid #FF9800;">
                        <div style="display: flex; align-items: center; margin-bottom: 8px;">
                            <span style="font-size: 1.5rem; margin-right: 10px;">↕️</span>
                            <strong style="color: {COLORS['primary']}; font-size: 0.95rem;">Eixo Vertical (Y)</strong>
                        </div>
                        <p style="margin: 0; font-size: 0.85rem; color: #555; line-height: 1.4;">
                            <strong>Media Power:</strong> Poder de broadcast. Mede quantas pessoas são alcançadas simultaneamente. Destaca <em>grande alcance</em>
                        </p>
                    </div>
                </div>
                <div style="background: {COLORS['primary']}; color: white; padding: 10px 15px; border-radius: 8px; margin-top: 15px; font-size: 0.85rem; text-align: center;">
                    💡 <strong>Insight:</strong> Influenciadores no <strong>canto superior direito</strong> possuem tanto alcance quanto engajamento alto
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Ajustar tamanho das bolhas dinamicamente baseado na quantidade de dados
        num_influencers = len(dff['nickName'].unique())
        # Quanto menos influenciadores, maior o tamanho máximo das bolhas
        size_max_dynamic = max(50, min(80, 150 - (num_influencers * 2)))
        
        fig_b = px.scatter(dff, x='socialPowers', y='mediaPowers', size='audienceSizes', 
                           color='MicroTrends', hover_name='nickName', size_max=size_max_dynamic)
        
        # Configurar layout otimizado
        fig_b.update_layout(
            height=700,
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.15,
                xanchor="center",
                x=0.5,
                font=dict(size=11)
            ),
            xaxis_title="Social Power",
            yaxis_title="Media Power",
            margin=dict(l=50, r=50, t=30, b=120),
            # Ajustar escala dos eixos para melhor visualização
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(200,200,200,0.2)',
                zeroline=True,
                zerolinecolor='rgba(200,200,200,0.5)'
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(200,200,200,0.2)',
                zeroline=True,
                zerolinecolor='rgba(200,200,200,0.5)'
            )
        )
        
        # Melhorar o hover template
        fig_b.update_traces(
            hovertemplate='<b>%{hovertext}</b><br><br>' +
                         'Social Power: %{x:.4f}<br>' +
                         'Media Power: %{y:.0f}<br>' +
                         'Audiência: %{marker.size:,.0f}<br>' +
                         '<extra></extra>'
        )
        
        st.plotly_chart(fig_b, use_container_width=True)

        # 4. Lista de Influenciadores (Ranking Reativo)
        st.markdown("---")
        st.subheader("Top 10 Influenciadores por Alcance")
        
        ranking = dff.groupby('nickName').agg({
            'video_id': 'count', 'audienceSizes': 'sum', 'engajamento': 'sum',
            'followers': 'max', 'Desc': 'first', 'link': 'first'
        }).sort_values('followers', ascending=False).head(10)

        for nick, row in ranking.iterrows():
            st.markdown(f"""
                <div class="influencer-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 1.3rem; font-weight: bold; color: {COLORS['primary']};">{nick}</span>
                        <a href="{row['link']}" target="_blank" class="btn-link">VER VÍDEO</a>
                    </div>
                    <div style="display: flex; gap: 30px; margin-top: 15px;">
                        <div><small>VIEWS</small><br><b>{format_num(row['engajamento'])}</b></div>
                        <div><small>SEGUIDORES</small><br><b>{format_num(row['followers'])}</b></div>
                        <div><small>AUDIÊNCIA</small><br><b>{format_num(row['audienceSizes'])}</b></div>
                        <div><small>VÍDEOS</small><br><b>{int(row['video_id'])}</b></div>
                    </div>
                    <div style="margin-top: 15px; color: #555; font-size: 0.9rem; border-top: 1px solid #f0f0f0; padding-top: 10px;">
                        {str(row['Desc'])[:300]}...
                    </div>
                </div>
            """, unsafe_allow_html=True)
else:
    st.error("Base de dados não encontrada ou vazia.")