# src/i18n/strings.py
"""
Internationalisation (i18n) string dictionary for AstroEduPlanner (AEOP).

Usage in app.py:
    from src.i18n.strings import LANGUAGES
    t = LANGUAGES[language]
    st.title(t["app_title"])
"""

LANGUAGES = {

    # ------------------------------------------------------------------ #
    #  ENGLISH                                                             #
    # ------------------------------------------------------------------ #
    "English": {
        # Page config
        "page_title":               "AstroEduPlanner",
        "page_icon":                "🔭",

        # App title
        "app_title":                "🔭 Astronomical Visibility Planner",

        # Sidebar – general
        "sidebar_header":           "Analysis Settings",
        "language_label":           "🌐 Language / Idioma",

        # Sidebar – location
        "location_subheader":       "📍 Observer Location",
        "location_method_label":    "Location Method",
        "location_method_city":     "City",
        "location_method_coords":   "Coordinates",
        "city_input_label":         "City",
        "city_input_default":       "São Paulo, Brazil",
        "city_button":              "Set Location",
        "city_spinner":             "Searching coordinates for {city}…",
        "coords_input_label":       "Latitude, Longitude",
        "coords_input_placeholder": "-22.90,-43.17",
        "coords_button":            "Set by Coordinates",
        "coords_invalid_error":     "Invalid format. Please use 'lat,lon' (e.g. -22.90,-43.17).",
        "location_set_success":     "Location set: {lat:.2f}°, {lon:.2f}°",
        "location_cached_info":     "Cached location: {lat:.2f}°, {lon:.2f}°",
        "location_missing_warning": "Please set an observer location.",

        # Sidebar – parameters
        "date_input_label":         "Observation Date",
        "min_alt_label":            "Minimum Elevation (°)",

        # Tabs
        "tab_nightly":              "🌙 Nightly Analysis",
        "tab_annual":               "📅 Annual Calendar",

        # --- Nightly analysis tab ---
        "nightly_header":           "Visibility Analysis for the Selected Night",
        "checkbox_deep_sky":        "Include Deep-Sky Targets",
        "checkbox_solar_system":    "Include Solar System Targets",
        "manual_targets_label":     "Add targets manually (one per line)",
        "manual_targets_default":   "M83\nNGC 1365",
        "run_nightly_button":       "Generate Nightly Analysis",
        "no_location_error":        "Please set an observer location before running the analysis.",
        "nightly_spinner":          "Computing nightly events…",
        "nightly_events_error":     "Could not compute nightly events for this date and location.",

        # Night info box
        "night_info_title":         "Night Information ({date})",
        "night_sunset":             "🌅 Sunset",
        "night_start":              "🌌 Night Start (Astronomical Twilight)",
        "night_end":                "🌄 Night End",
        "night_sunrise":            "☀️ Sunrise",
        "time_utc_suffix":          "UTC",

        # Target fetching
        "fetching_coords_spinner":  "Fetching coordinates for {n} targets…",
        "solar_system_spinner":     "Computing Solar System positions…",
        "no_targets_warning":       "No targets were selected or found.",
        "analysing_targets":        "Analysing {n} targets…",

        # Per-target results
        "obs_window_label":         "**Observation Window Duration:** {dur:.2f} h",
        "max_alt_label":            "**Maximum Altitude:** {alt:.1f}°",
        "target_not_visible":       "❌ {name}: Not visible above {min}° on the selected date.",

        # Sky map
        "sky_map_subheader":        "🗺️ Night Sky Map",
        "sky_map_description":      "View all visible targets in the sky at a selected time.",
        "sky_map_slider":           "Select time (UTC)",
        "sky_map_button":           "Generate Map",
        "sky_map_success":          "🗺️ Sky map — {n} target(s) visible at {h:02d}:00 UTC",
        "sky_map_how_to_read":      """**How to read the map:**
- The centre represents the zenith (directly overhead)
- The outer edge represents the horizon
- N, S, E, W mark the cardinal directions
- Each dot is a visible target""",
        "sky_map_no_targets":       "No targets visible above {min}° at {h:02d}:00 UTC.",
        "sky_map_error":            "Error generating sky map: {err}",

        # --- Annual calendar tab ---
        "annual_header":            "Annual Visibility Calendar",
        "annual_target_label":      "Target Name",
        "annual_target_default":    "M31",
        "annual_year_label":        "Year",
        "annual_button":            "Generate Annual Calendar",
        "annual_target_spinner":    "Fetching coordinates for {name}…",
        "annual_target_error":      "Could not find target '{name}'. Please check the name and try again.",
        "annual_analysis_spinner":  "Analysing visibility of {name} throughout {year}… This may take a few minutes.",
        "annual_no_data":           "Target {name} was not visible above {min}° on any night in {year} at this location.",
        "annual_success":           "Analysis complete! {name} was visible on {n} nights during {year}.",
        "stats_subheader":          "📊 Statistics",
        "stat_visible_nights":      "Visible Nights",
        "stat_avg_duration":        "Average Duration",
        "stat_max_duration":        "Maximum Duration",
        "best_period":              "🌟 **Best Period:** {month} {year}",
        "month_names": [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ],
    },

    # ------------------------------------------------------------------ #
    #  PORTUGUÊS                                                           #
    # ------------------------------------------------------------------ #
    "Português": {
        # Page config
        "page_title":               "AstroEduPlanner",
        "page_icon":                "🔭",

        # App title
        "app_title":                "🔭 Analisador de Visibilidade Astronômica",

        # Sidebar – general
        "sidebar_header":           "Configurações da Análise",
        "language_label":           "🌐 Language / Idioma",

        # Sidebar – location
        "location_subheader":       "📍 Localização do Observador",
        "location_method_label":    "Método de Localização",
        "location_method_city":     "Cidade",
        "location_method_coords":   "Coordenadas",
        "city_input_label":         "Cidade",
        "city_input_default":       "São Paulo, Brazil",
        "city_button":              "Definir por Cidade",
        "city_spinner":             "Buscando coordenadas para {city}…",
        "coords_input_label":       "Latitude, Longitude",
        "coords_input_placeholder": "-22.90,-43.17",
        "coords_button":            "Definir por Coordenadas",
        "coords_invalid_error":     "Formato inválido. Use 'lat,lon' (ex.: -22.90,-43.17).",
        "location_set_success":     "Localização definida: {lat:.2f}°, {lon:.2f}°",
        "location_cached_info":     "Localização em cache: {lat:.2f}°, {lon:.2f}°",
        "location_missing_warning": "Por favor, defina uma localização do observador.",

        # Sidebar – parameters
        "date_input_label":         "Data da Análise Noturna",
        "min_alt_label":            "Elevação Mínima (°)",

        # Tabs
        "tab_nightly":              "🌙 Análise Noturna",
        "tab_annual":               "📅 Calendário Anual",

        # --- Nightly analysis tab ---
        "nightly_header":           "Análise de Visibilidade para a Noite Selecionada",
        "checkbox_deep_sky":        "Incluir Alvos de Céu Profundo",
        "checkbox_solar_system":    "Incluir Alvos do Sistema Solar",
        "manual_targets_label":     "Adicionar alvos manualmente (um por linha)",
        "manual_targets_default":   "M83\nNGC 1365",
        "run_nightly_button":       "Gerar Análise da Noite",
        "no_location_error":        "A localização do observador deve ser definida antes de executar a análise.",
        "nightly_spinner":          "Calculando eventos noturnos…",
        "nightly_events_error":     "Não foi possível calcular os eventos noturnos para esta data e localização.",

        # Night info box
        "night_info_title":         "Informações da Noite ({date})",
        "night_sunset":             "🌅 Pôr do Sol",
        "night_start":              "🌌 Início da Noite (Crepúsculo Astronômico)",
        "night_end":                "🌄 Fim da Noite",
        "night_sunrise":            "☀️ Nascer do Sol",
        "time_utc_suffix":          "UTC",

        # Target fetching
        "fetching_coords_spinner":  "Buscando coordenadas de {n} alvos…",
        "solar_system_spinner":     "Calculando posições do Sistema Solar…",
        "no_targets_warning":       "Nenhum alvo foi selecionado ou encontrado.",
        "analysing_targets":        "Analisando visibilidade de {n} alvos…",

        # Per-target results
        "obs_window_label":         "**Duração da Janela de Observação:** {dur:.2f} h",
        "max_alt_label":            "**Altitude Máxima:** {alt:.1f}°",
        "target_not_visible":       "❌ {name}: Não visível acima de {min}° na data selecionada.",

        # Sky map
        "sky_map_subheader":        "🗺️ Mapa do Céu Noturno",
        "sky_map_description":      "Visualize a posição de todos os alvos visíveis no céu em um momento específico.",
        "sky_map_slider":           "Selecione o horário (UTC)",
        "sky_map_button":           "Gerar Mapa",
        "sky_map_success":          "🗺️ Mapa do céu — {n} alvo(s) visível(is) às {h:02d}:00 UTC",
        "sky_map_how_to_read":      """**Como interpretar o mapa:**
- O centro representa o zênite (diretamente acima)
- A borda externa representa o horizonte
- N, S, L, O indicam as direções cardeais
- Cada ponto é um alvo visível""",
        "sky_map_no_targets":       "Nenhum alvo está visível acima de {min}° às {h:02d}:00 UTC.",
        "sky_map_error":            "Erro ao gerar mapa do céu: {err}",

        # --- Annual calendar tab ---
        "annual_header":            "Calendário de Visibilidade Anual",
        "annual_target_label":      "Nome do Alvo",
        "annual_target_default":    "M31",
        "annual_year_label":        "Ano",
        "annual_button":            "Gerar Calendário Anual",
        "annual_target_spinner":    "Buscando coordenadas de {name}…",
        "annual_target_error":      "Não foi possível encontrar o alvo '{name}'. Verifique o nome e tente novamente.",
        "annual_analysis_spinner":  "Analisando visibilidade de {name} ao longo de {year}… Isso pode levar alguns minutos.",
        "annual_no_data":           "O alvo {name} não foi visível acima de {min}° em nenhuma noite de {year} nesta localização.",
        "annual_success":           "Análise concluída! {name} foi visível em {n} noites durante {year}.",
        "stats_subheader":          "📊 Estatísticas",
        "stat_visible_nights":      "Noites Visíveis",
        "stat_avg_duration":        "Duração Média",
        "stat_max_duration":        "Duração Máxima",
        "best_period":              "🌟 **Melhor Período:** {month} de {year}",
        "month_names": [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ],
    },
}
