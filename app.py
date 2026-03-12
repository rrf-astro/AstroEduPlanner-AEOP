# app.py
# Arquivo principal da aplicação web com Streamlit

import streamlit as st
from datetime import date, timedelta
import pytz

# Importar as funções do backend
from src.config import *
from src.location import get_location_from_city, set_timezone_for_sao_paulo
from src.targets import get_target_skycoords, registrar_alvos_sistema_solar, DEEP_SKY_TARGETS_PRESET
from src.analysis import calculate_nightly_events, analyze_target_visibility_for_night, analyze_year_visibility
from src.plotting import plot_target_visibility, plot_yearly_visibility, plot_sky_map

# --- Configuração da Página ---
st.set_page_config(page_title="Analisador Astronômico", page_icon="🔭", layout="wide")
st.title("🔭 Analisador de Visibilidade Astronômica")

# --- Barra Lateral de Controles ---
st.sidebar.header("Configurações da Análise")

# 1. Localização
st.sidebar.subheader("📍 Localização do Observador")
location_method = st.sidebar.radio("Método de Localização", ('Cidade', 'Coordenadas'))
observer_location = None

if location_method == 'Cidade':
    city_name = st.sidebar.text_input("Cidade", "São Paulo, Brazil")
    if st.sidebar.button("Definir por Cidade"):
        with st.spinner(f"Buscando coordenadas para {city_name}..."):
            observer_location = get_location_from_city(city_name)
else:
    lat_lon_str = st.sidebar.text_input("Latitude,Longitude", "-22.90,-43.17") # Rio de Janeiro
    if st.sidebar.button("Definir por Coordenadas"):
        try:
            lat, lon = map(float, lat_lon_str.split(','))
            observer_location = EarthLocation(lat=lat*u.deg, lon=lon*u.deg)
        except ValueError:
            st.sidebar.error("Formato inválido. Use 'lat,lon'.")

if observer_location is not None:
    st.session_state['observer_location'] = observer_location
    st.sidebar.success(f"Localização definida: {observer_location.lat.deg:.2f}, {observer_location.lon.deg:.2f}")
elif 'observer_location' in st.session_state:
    observer_location = st.session_state['observer_location']
    st.sidebar.info(f"Localização em cache: {observer_location.lat.deg:.2f}, {observer_location.lon.deg:.2f}")
else:
    st.sidebar.warning("Defina uma localização.")


# 2. Parâmetros
analysis_date = st.sidebar.date_input("Data da Análise Noturna", date.today())
min_altitude_deg = st.sidebar.slider("Elevação Mínima (°)", 10, 90, 30)
min_altitude = min_altitude_deg * u.deg

# --- Abas para diferentes análises ---
tab1, tab2 = st.tabs(["🌙 Análise Noturna", "📅 Calendário Anual"])

# ... (Lógica das abas como antes) ...
with tab1:
    st.header("Análise de Visibilidade para a Noite Selecionada")
    col1, col2 = st.columns(2)
    with col1:
        use_deep_sky = st.checkbox("Incluir Alvos de Céu Profundo", True)
        use_solar_system = st.checkbox("Incluir Alvos do Sistema Solar", True)
    with col2:
        manual_targets_input = st.text_area("Adicionar alvos manualmente (um por linha)", "M83\\nNGC 1365")

    if st.button("Gerar Análise da Noite", type="primary"):
        if 'observer_location' not in st.session_state:
            st.error("A localização do observador deve ser definida antes de executar a análise.")
        else:
            observer_location = st.session_state['observer_location']
            observer_timezone = set_timezone_for_sao_paulo(observer_location) or pytz.UTC
            
            with st.spinner("Calculando eventos noturnos..."):
                night_events = calculate_nightly_events(analysis_date, observer_location, observer_timezone)
            
            if not night_events:
                st.error("Não foi possível calcular os eventos noturnos para esta data e localização.")
            else:
                start_night = night_events['inicio_noite']
                end_night = night_events['fim_noite']
                
                # Exibir informações da noite
                st.info(f"""
                **Informações da Noite ({analysis_date.strftime('%d/%m/%Y')})**
                - 🌅 Pôr do Sol: {night_events['por_do_sol'].to_datetime():%H:%M UTC}
                - 🌌 Início da Noite (Crepúsculo Astronômico): {start_night.to_datetime():%H:%M UTC}
                - 🌄 Fim da Noite: {end_night.to_datetime():%H:%M UTC}
                - ☀️ Nascer do Sol: {night_events['nascer_do_sol'].to_datetime():%H:%M UTC}
                """)
                
                # Coletar nomes de alvos
                target_names = []
                if use_deep_sky:
                    target_names.extend(DEEP_SKY_TARGETS_PRESET)
                
                if manual_targets_input.strip():
                    manual_targets = [line.strip() for line in manual_targets_input.split('\\n') if line.strip()]
                    target_names.extend(manual_targets)
                
                # Buscar coordenadas dos alvos
                all_targets = {}
                if target_names:
                    with st.spinner(f"Buscando coordenadas de {len(target_names)} alvos..."):
                        all_targets.update(get_target_skycoords(target_names))
                
                # Adicionar alvos do sistema solar
                if use_solar_system:
                    with st.spinner("Calculando posições do Sistema Solar..."):
                        all_targets.update(registrar_alvos_sistema_solar(start_night))
                
                if not all_targets:
                    st.warning("Nenhum alvo foi selecionado ou encontrado.")
                else:
                    st.success(f"Analisando visibilidade de {len(all_targets)} alvos...")
                    
                    # Analisar e plotar cada alvo
                    for target_name, target_coord in all_targets.items():
                        if target_coord is not None:
                            df_visible = analyze_target_visibility_for_night(
                                start_night, end_night, observer_location, target_coord, min_altitude
                            )
                            
                            if not df_visible.empty:
                                st.subheader(f"✅ {target_name}")
                                
                                # Gerar e exibir o gráfico
                                fig = plot_target_visibility(df_visible, target_name, analysis_date, min_altitude_deg)
                                st.pyplot(fig)
                                plt.close(fig)
                                
                                # Informações adicionais
                                duration = (df_visible['time'].iloc[-1] - df_visible['time'].iloc[0]).total_seconds() / 3600.0
                                max_alt = df_visible['altitude'].max()
                                st.write(f"**Duração da Janela de Observação:** {duration:.2f} horas")
                                st.write(f"**Altitude Máxima:** {max_alt:.1f}°")
                            else:
                                st.warning(f"❌ {target_name}: Não visível acima de {min_altitude_deg}° na data selecionada.")
                    
                    # Mapa do Céu Noturno
                    st.markdown("---")
                    st.subheader("🗺️ Mapa do Céu Noturno")
                    st.write("Visualize a posição de todos os alvos visíveis no céu em um momento específico.")
                    
                    # Seletor de horário com slider
                    midnight_hour = night_events['meia_noite_real'].to_datetime().hour
                    
                    col1, col2 = st.columns([4, 1])
                    with col1:
                        selected_hour = st.slider(
                            "Selecione o horário (UTC)", 
                            min_value=0, 
                            max_value=23, 
                            value=midnight_hour,
                            step=1,
                            format="%d:00",
                            help="Arraste para escolher a hora do mapa do céu"
                        )
                    with col2:
                        st.write("")  # Espaçamento
                        st.write("")  # Espaçamento
                        if st.button("Gerar Mapa", key="sky_map_button", type="primary"):
                            try:
                                # Converter horário do slider para Time object
                                hour = selected_hour
                                map_datetime = analysis_date.replace(hour=hour, minute=0) if hour >= 12 else \
                                              (analysis_date + timedelta(days=1)).replace(hour=hour, minute=0)
                                map_time = Time(map_datetime)
                                
                                # Filtrar apenas alvos visíveis neste horário
                                visible_at_time = {}
                                frame = AltAz(obstime=map_time, location=observer_location)
                                for name, coord in all_targets.items():
                                    if coord is not None:
                                        altaz = coord.transform_to(frame)
                                        if altaz.alt.deg >= min_altitude_deg:
                                            visible_at_time[name] = coord
                                
                                if visible_at_time:
                                    st.success(f"🗺️ Mapa do céu com {len(visible_at_time)} alvos visíveis às {hour:02d}:00 UTC")
                                    
                                    # Gerar e exibir o mapa
                                    fig = plot_sky_map(visible_at_time, observer_location, map_time)
                                    st.pyplot(fig)
                                    plt.close(fig)
                                    
                                    st.info("""
                                    **Como interpretar o mapa:**
                                    - O centro representa o zênite (diretamente acima)
                                    - A borda externa representa o horizonte
                                    - N, S, L, O indicam as direções cardeais
                                    - Cada ponto é um alvo visível
                                    """)
                                else:
                                    st.warning(f"Nenhum alvo está visível acima de {min_altitude_deg}° às {hour:02d}:00 UTC")
                            except Exception as e:
                                st.error(f"Erro ao gerar mapa: {e}")
with tab2:
    st.header("Calendário de Visibilidade Anual")
    yearly_target_name = st.text_input("Nome do Alvo", "M31", key="yearly_target")
    year = st.number_input("Ano", value=date.today().year, min_value=1900, max_value=2100, key="yearly_year")

    if st.button("Gerar Calendário Anual", type="primary", key="yearly_button"):
        if 'observer_location' not in st.session_state:
            st.error("A localização do observador deve ser definida antes de executar a análise.")
        else:
            observer_location = st.session_state['observer_location']
            observer_timezone = set_timezone_for_sao_paulo(observer_location) or pytz.UTC
            
            # Buscar coordenadas do alvo
            with st.spinner(f"Buscando coordenadas de {yearly_target_name}..."):
                target_coords = get_target_skycoords([yearly_target_name])
            
            if yearly_target_name not in target_coords or target_coords[yearly_target_name] is None:
                st.error(f"Não foi possível encontrar o alvo '{yearly_target_name}'. Verifique o nome e tente novamente.")
            else:
                target_coord = target_coords[yearly_target_name]
                
                # Realizar análise anual (pode levar alguns minutos)
                with st.spinner(f"Analisando visibilidade de {yearly_target_name} ao longo de {year}... Isso pode levar alguns minutos."):
                    df_year = analyze_year_visibility(year, observer_location, observer_timezone, target_coord, min_altitude)
                
                if df_year.empty:
                    st.warning(f"O alvo {yearly_target_name} não foi visível acima de {min_altitude_deg}° em nenhuma noite de {year} nesta localização.")
                else:
                    st.success(f"Análise anual concluída! {yearly_target_name} foi visível em {len(df_year)} noites durante {year}.")
                    
                    # Gerar e exibir o heatmap
                    fig = plot_yearly_visibility(df_year, yearly_target_name, year)
                    if fig:
                        st.pyplot(fig)
                        plt.close(fig)
                    
                    # Estatísticas adicionais
                    st.subheader("📊 Estatísticas")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Noites Visíveis", len(df_year))
                    with col2:
                        avg_duration = df_year['duration_hours'].mean()
                        st.metric("Duração Média", f"{avg_duration:.2f}h")
                    with col3:
                        max_duration = df_year['duration_hours'].max()
                        st.metric("Duração Máxima", f"{max_duration:.2f}h")
                    
                    # Melhor período
                    best_month = df_year.groupby(pd.to_datetime(df_year['date']).dt.month)['duration_hours'].mean().idxmax()
                    month_names = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
                    st.info(f"🌟 **Melhor Período:** {month_names[best_month-1]} de {year}")
