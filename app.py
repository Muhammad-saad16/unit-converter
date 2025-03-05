# # import streamlit as st

# # # ✅ MUST BE FIRST STREAMLIT COMMAND
# # st.set_page_config(
# #     page_title="Ultimate Unit Converter",
# #     page_icon="📊",
# #     layout="wide"
# # )

# # # Initialize session state for theme
# # if 'theme' not in st.session_state:
# #     st.session_state.theme = 'System Default'

# # # Unit conversion data
# # unit_conversions = {
# #     'Length': {
# #         'meters': 1,
# #         'kilometers': 1000,
# #         'centimeters': 0.01,
# #         'millimeters': 0.001,
# #         'miles': 1609.34,
# #         'yards': 0.9144,
# #         'feet': 0.3048,
# #         'inches': 0.0254,
# #         'nautical miles': 1852
# #     },
# #     'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
# #     'Area': {
# #         'square meters': 1,
# #         'square kilometers': 1e6,
# #         'square miles': 2.59e6,
# #         'acres': 4046.86,
# #         'hectares': 10000,
# #         'square feet': 0.092903,
# #         'square inches': 0.00064516
# #     },
# #     'Data Transfer Rate': {
# #         'bits per second': 1,
# #         'bytes per second': 8,
# #         'kilobits per second': 1000,
# #         'megabits per second': 1e6,
# #         'gigabits per second': 1e9,
# #         'terabits per second': 1e12
# #     },
# #     'Digital Storage': {
# #         'bits': 1,
# #         'bytes': 8,
# #         'kilobytes': 8192,
# #         'megabytes': 8.389e+6,
# #         'gigabytes': 8.59e+9,
# #         'terabytes': 8.796e+12
# #     },
# #     'Energy': {
# #         'joules': 1,
# #         'kilojoules': 1000,
# #         'calories': 4.184,
# #         'kilocalories': 4184,
# #         'watthours': 3600,
# #         'kilowatthours': 3.6e6
# #     },
# #     'Frequency': {
# #         'hertz': 1,
# #         'kilohertz': 1e3,
# #         'megahertz': 1e6,
# #         'gigahertz': 1e9,
# #         'terahertz': 1e12
# #     },
# #     'Fuel Economy': {
# #         'miles per gallon': 1,
# #         'kilometers per liter': 2.352,
# #         'liters per 100 km': 235.215
# #     },
# #     'Mass': {
# #         'grams': 1,
# #         'kilograms': 1000,
# #         'milligrams': 0.001,
# #         'pounds': 453.592,
# #         'ounces': 28.3495,
# #         'tons': 907185
# #     },
# #     'Plane Angle': {
# #         'degrees': 1,
# #         'radians': 57.2958,
# #         'gradians': 0.9
# #     },
# #     'Pressure': {
# #         'pascals': 1,
# #         'kilopascals': 1000,
# #         'bars': 1e5,
# #         'atmospheres': 101325,
# #         'psi': 6894.76
# #     },
# #     'Speed': {
# #         'meters per second': 1,
# #         'kilometers per hour': 0.277778,
# #         'miles per hour': 0.44704,
# #         'knots': 0.514444,
# #         'mach': 343
# #     },
# #     'Time': {
# #         'seconds': 1,
# #         'minutes': 60,
# #         'hours': 3600,
# #         'days': 86400,
# #         'weeks': 604800,
# #         'years': 31536000
# #     },
# #     'Volume': {
# #         'liters': 1,
# #         'milliliters': 0.001,
# #         'cubic meters': 1000,
# #         'gallons': 3.78541,
# #         'quarts': 0.946353,
# #         'pints': 0.473176,
# #         'cups': 0.24,
# #         'fluid ounces': 0.0295735
# #     }
# # }

# # def convert_temperature(value, from_unit, to_unit):
# #     conversion_functions = {
# #         ('Celsius', 'Fahrenheit'): lambda x: (x * 9/5) + 32,
# #         ('Celsius', 'Kelvin'): lambda x: x + 273.15,
# #         ('Fahrenheit', 'Celsius'): lambda x: (x - 32) * 5/9,
# #         ('Fahrenheit', 'Kelvin'): lambda x: (x - 32) * 5/9 + 273.15,
# #         ('Kelvin', 'Celsius'): lambda x: x - 273.15,
# #         ('Kelvin', 'Fahrenheit'): lambda x: (x - 273.15) * 9/5 + 32
# #     }
# #     return conversion_functions[(from_unit, to_unit)](value) if from_unit != to_unit else value

# # theme_styles = {
# #     "Light": {
# #         "--background-color": "#ffffff",
# #         "--text-color": "#000000",
# #         "--primary-color": "#1f77b4",
# #         "--secondary-color": "#ff7f0e",
# #         "--card-background": "#f0f2f6",
# #         "--sidebar-background": "#f0f2f6",
# #         "--sidebar-text": "#000000",
# #         "--sidebar-select-text": "#000000"
# #     },
# #     "Dark": {
# #         "--background-color": "#0e1117",
# #         "--text-color": "#ffffff",
# #         "--primary-color": "#00ffff",
# #         "--secondary-color": "#00ff00",
# #         "--card-background": "#1a1c24",
# #         "--sidebar-background": "#000000",  # Pure black
# #         "--sidebar-text": "#ffffff",
# #         "--sidebar-select-text": "#ffffff"
# #     },
# #     "System Default": {
# #         "--background-color": "inherit",
# #         "--text-color": "inherit",
# #         "--primary-color": "#1f77b4",
# #         "--secondary-color": "#ff7f0e",
# #         "--card-background": "inherit",
# #         "--sidebar-background": "inherit",
# #         "--sidebar-text": "inherit",
# #         "--sidebar-select-text": "inherit"
# #     }
# # }

# # # Sidebar with theme selector
# # with st.sidebar:
# #     st.header("🌟 Features & Settings")
# #     st.session_state.theme = st.selectbox(
# #         "🎨 Theme Selector",
# #         ["Light", "Dark", "System Default"],
# #         index=["Light", "Dark", "System Default"].index(st.session_state.theme)
# #     )
    
# #     st.markdown("""
# #     - 15+ Conversion Categories
# #     - 100+ Supported Units
# #     - Real-time Updates
# #     - Scientific Precision
# #     - Mobile Friendly
# #     """)
# #     st.markdown("---")
# #     st.markdown("Made with ❤️ by **Muhammad Saad** using Streamlit")

# # # Update the Dynamic CSS styling section with this code
# # selected_style = theme_styles[st.session_state.theme]

# # css = f"""
# # <style>
# # [data-testid="stSidebar"] {{
# #     background-color: {selected_style.get('--sidebar-background', '')} !important;
# # }}

# # [data-testid="stSidebar"] * {{
# #     color: {selected_style.get('--sidebar-text', '')} !important;
# # }}

# # [data-testid="stSidebar"] .stSelectbox div {{
# #     background-color: {selected_style['--card-background']} !important;
# #     color: {selected_style.get('--sidebar-select-text', '')} !important;
# # }}

# # [data-testid="stSidebar"] .stMarkdown {{
# #     color: {selected_style.get('--sidebar-text', '')} !important;
# # }}

# # [data-testid="stSidebar"] hr {{
# #     border-color: {selected_style.get('--primary-color', '')} !important;
# # }}

# # [data-testid="stSidebar"] .st-emotion-cache-1oe5can {{
# #     background-color: {selected_style.get('--sidebar-background', '')} !important;
# # }}
# # [data-testid="stAppViewContainer"] {{
# #     background-color: {selected_style.get('--background-color', '')} !important;
# #     color: {selected_style.get('--text-color', '')} !important;
# # }}

# # [data-testid="stHeader"] {{
# #     background-color: {selected_style.get('--card-background', '')} !important;
# # }}

# # [data-testid="stToolbar"] {{
# #     color: {selected_style.get('--text-color', '')} !important;
# # }}

# # [data-testid="stSelectbox"] div {{
# #     background-color: {selected_style.get('--card-background', '')} !important;
# #     color: {selected_style.get('--text-color', '')} !important;
# # }}

# # [data-testid="stNumberInput"] input {{
# #     background-color: {selected_style.get('--card-background', '')} !important;
# #     color: {selected_style.get('--text-color', '')} !important;
# # }}

# # [data-testid="stExpander"] {{
# #     background-color: {selected_style.get('--card-background', '')} !important;
# #     border-color: {selected_style.get('--primary-color', '')} !important;
# # }}

# # .st-bq {{
# #     border-color: {selected_style.get('--primary-color', '')} !important;
# # }}

# # .conversion-card {{
# #     background: {selected_style.get('--card-background', '')} !important;
# #     color: {selected_style.get('--text-color', '')} !important;
# #     border-radius: 10px;
# #     padding: 20px;
# #     margin-top: 20px;
# #     border: 1px solid {selected_style.get('--primary-color', '')} !important;
# # }}

# # h1, h2, h3 {{
# #     color: {selected_style.get('--primary-color', '')} !important;
# # }}

# # .st-emotion-cache-cio0dv {{
# #     background-color: {selected_style.get('--background-color', '')} !important;
# # }}
# # </style>
# # """

# # # Apply custom CSS for responsiveness and styling
# # st.markdown(
# #     """
# #     <style>
# #         /* Responsive Title Styling */
# #         h1 {
# #             font-size: 3rem !important;
# #             text-align: center;
# #             color: #4CAF50 !important; /* Green color */
# #         }

# #         h3 {
# #             font-size: 1.8rem !important;
# #             text-align: center;
# #             color: #2196F3 !important; /* Blue color */
# #         }

# #         /* Responsive Design */
# #         @media (max-width: 1024px) {
# #             h1 { font-size: 2.5rem !important; }
# #             h3 { font-size: 1.6rem !important; }
# #         }

# #         @media (max-width: 768px) {
# #             h1 { font-size: 2.2rem !important; }
# #             h3 { font-size: 1.4rem !important; }
# #         }

# #         @media (max-width: 480px) {
# #             h1 { font-size: 2rem !important; }
# #             h3 { font-size: 1.2rem !important; }
# #         }
# #     </style>
# #     """,
# #     unsafe_allow_html=True
# # )

# # st.markdown(css, unsafe_allow_html=True)

# # # Main app interface
# # st.title("🚀 Ultimate Unit Converter")
# # st.markdown("### ⚡ Real-time Conversion | 15+ Categories | 100+ Units")

# # with st.container():
# #     category = st.selectbox("📌 Select Category", list(unit_conversions.keys()))
    
# #     col1, col2, col3 = st.columns([2,2,3])
# #     with col1:
# #         if category == 'Temperature':
# #             from_unit = st.selectbox("From", unit_conversions[category])
# #         else:
# #             from_unit = st.selectbox("From", list(unit_conversions[category].keys()))
    
# #     with col2:
# #         if category == 'Temperature':
# #             to_unit = st.selectbox("To", unit_conversions[category])
# #         else:
# #             to_unit = st.selectbox("To", list(unit_conversions[category].keys()))
    
# #     with col3:
# #         value = st.number_input("Enter Value", min_value=0.0, value=1.0, step=0.1, format="%.4f")

# # # Conversion logic
# # if category == 'Temperature':
# #     result = convert_temperature(value, from_unit, to_unit)
# # else:
# #     from_factor = unit_conversions[category][from_unit]
# #     to_factor = unit_conversions[category][to_unit]
# #     result = (value * from_factor) / to_factor

# # # Display results
# # st.markdown(f"""
# # <div class="conversion-card">
# #     <h2 style="text-align:center;">
# #     🎯 Conversion Result: 
# #     <span style="color:{selected_style.get('--secondary-color', '#00ff00')}">{value:.4f} {from_unit}</span> = 
# #     <span style="color:{selected_style.get('--primary-color', '#00ffff')}">{result:.6f} {to_unit}</span>
# #     </h2>
# # </div>
# # """, unsafe_allow_html=True)

# # with st.expander("📚 View Conversion Formulas"):
# #     st.write("""
# #     **Length:** Base Unit = meters  
# #     **Temperature:** Special formulas used  
# #     **Digital Storage:** 1 byte = 8 bits  
# #     **Speed:** 1 m/s = 3.6 km/h  
# #     **Fuel Economy:** 1 mile/gallon ≈ 2.352 km/liter  
# #     """)
# import streamlit as st

# # ✅ Set App Config (Dark Theme Default)
# st.set_page_config(
#     page_title="Ultimate Unit Converter 🚀",
#     page_icon="📊",
#     layout="wide"
# )

# # Initialize session state for theme
# if 'theme' not in st.session_state:
#     st.session_state.theme = 'Dark'  # Default to Dark Theme

# # Define Enhanced Theme Styles
# theme_styles = {
#     "Light": {
#         "--background-color": "#ffffff",
#         "--text-color": "#000000",
#         "--primary-color": "#1f77b4",
#         "--secondary-color": "#ff7f0e",
#         "--card-background": "#f8f9fa",
#         "--sidebar-background": "#f0f2f6"
#     },
#     "Dark": {
#         "--background-color": "#121212",
#         "--text-color": "#ffffff",
#         "--primary-color": "#00ffff",
#         "--secondary-color": "#ff4081",
#         "--card-background": "#1e1e1e",
#         "--sidebar-background": "#1c1c1c"
#     }
# }

# # Sidebar with Theme Selector
# with st.sidebar:
#     st.markdown("<h2 style='text-align:center;'>🎨 Customize Theme</h2>", unsafe_allow_html=True)
#     st.session_state.theme = st.radio(
#         "Choose Theme:", ["Dark", "Light"], index=0 if st.session_state.theme == "Dark" else 1
#     )

# # Apply Selected Theme
# selected_style = theme_styles[st.session_state.theme]

# # Modern Animated CSS
# css = f"""
# <style>
# /* General Styling */
# [data-testid="stAppViewContainer"] {{
#     background: {selected_style['--background-color']} !important;
#     color: {selected_style['--text-color']} !important;
# }}

# /* Sidebar Styling */
# [data-testid="stSidebar"] {{
#     background: linear-gradient(45deg, {selected_style['--sidebar-background']}, #333333) !important;
#     border-right: 2px solid {selected_style['--primary-color']} !important;
# }}
# [data-testid="stSidebar"] * {{
#     color: {selected_style['--text-color']} !important;
# }}
# .st-emotion-cache-1oe5can {{
#     background-color: {selected_style['--sidebar-background']} !important;
# }}

# /* Card Styling with 3D Effect */
# .conversion-card {{
#     background: linear-gradient(145deg, {selected_style['--card-background']}, #292929);
#     box-shadow: 5px 5px 15px #000000, -5px -5px 15px #3a3a3a;
#     border-radius: 15px;
#     padding: 20px;
#     margin-top: 20px;
#     border: 2px solid {selected_style['--primary-color']} !important;
# }}

# /* Animated Button */
# .stButton>button {{
#     border-radius: 10px;
#     background: linear-gradient(to right, {selected_style['--primary-color']}, {selected_style['--secondary-color']});
#     color: white !important;
#     padding: 10px 20px;
#     font-size: 16px;
#     border: none;
#     transition: all 0.3s ease-in-out;
# }}
# .stButton>button:hover {{
#     transform: scale(1.1);
#     background: linear-gradient(to left, {selected_style['--primary-color']}, {selected_style['--secondary-color']});
# }}

# /* Fancy Headings */
# h1, h2, h3 {{
#     color: {selected_style['--primary-color']} !important;
#     text-align: center;
# }}
# </style>
# """
# st.markdown(css, unsafe_allow_html=True)

# # Main App Interface
# st.title("🚀 Ultimate Unit Converter")
# st.markdown("### ⚡ 15+ Categories | 100+ Units | Sleek Modern UI")

# # Unit conversion categories
# unit_conversions = {
#     'Length': {'meters': 1, 'kilometers': 1000, 'miles': 1609.34, 'yards': 0.9144, 'feet': 0.3048},
#     'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
#     'Mass': {'grams': 1, 'kilograms': 1000, 'pounds': 453.592, 'ounces': 28.3495},
#     'Time': {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400},
#     'Speed': {'meters per second': 1, 'kilometers per hour': 0.277778, 'miles per hour': 0.44704},
#     'Volume': {'liters': 1, 'milliliters': 0.001, 'gallons': 3.78541}
# }

# # Temperature Conversion Function
# def convert_temperature(value, from_unit, to_unit):
#     conversion = {
#         ('Celsius', 'Fahrenheit'): lambda x: (x * 9/5) + 32,
#         ('Celsius', 'Kelvin'): lambda x: x + 273.15,
#         ('Fahrenheit', 'Celsius'): lambda x: (x - 32) * 5/9,
#         ('Fahrenheit', 'Kelvin'): lambda x: (x - 32) * 5/9 + 273.15,
#         ('Kelvin', 'Celsius'): lambda x: x - 273.15,
#         ('Kelvin', 'Fahrenheit'): lambda x: (x - 273.15) * 9/5 + 32
#     }
#     return conversion.get((from_unit, to_unit), lambda x: x)(value)

# # UI Layout
# with st.container():
#     category = st.selectbox("📌 Select Category", list(unit_conversions.keys()))

#     col1, col2, col3 = st.columns([2,2,3])
#     with col1:
#         from_unit = st.selectbox("From", unit_conversions[category] if category == "Temperature" else list(unit_conversions[category].keys()))
#     with col2:
#         to_unit = st.selectbox("To", unit_conversions[category] if category == "Temperature" else list(unit_conversions[category].keys()))
#     with col3:
#         value = st.number_input("Enter Value", min_value=0.0, value=1.0, step=0.1, format="%.4f")

# # Conversion Logic
# if category == 'Temperature':
#     result = convert_temperature(value, from_unit, to_unit)
# else:
#     from_factor = unit_conversions[category][from_unit]
#     to_factor = unit_conversions[category][to_unit]
#     result = (value * from_factor) / to_factor

# # Display Results with Animation
# st.markdown(f"""
# <div class="conversion-card">
#     <h2 style="text-align:center; font-size:24px;">
#         🎯 {value:.4f} {from_unit} = <span style="color:{selected_style['--secondary-color']}">{result:.6f} {to_unit}</span>
#     </h2>
# </div>
# """, unsafe_allow_html=True)

# # Sidebar Info Section
# with st.sidebar:
#     st.markdown("<h3 style='text-align:center;'>📌 Features</h3>", unsafe_allow_html=True)
#     st.markdown("""
#     ✅ **15+ Conversion Categories**  
#     ✅ **100+ Supported Units**  
#     ✅ **Modern Dark UI**  
#     ✅ **Real-time Updates**  
#     ✅ **Scientific Precision**  
#     ✅ **Mobile Friendly**  
#     """)
#     st.markdown("---")
#     st.markdown("Made with ❤️ by **Muhammad Saad** using Streamlit 🚀")

# # Footer Animation
# st.markdown("""
# <style>
#     @keyframes glow {
#         0% { text-shadow: 0 0 5px #fff; }
#         50% { text-shadow: 0 0 15px {selected_style['--primary-color']}; }
#         100% { text-shadow: 0 0 5px #fff; }
#     }
#     .footer { text-align: center; font-size: 14px; animation: glow 2s infinite; }
# </style>
# <div class="footer">✨ Powered by OpenAI & Streamlit ✨</div>
# """, unsafe_allow_html=True)
import streamlit as st

# ✅ MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="🔥 Ultimate Unit Converter",
    page_icon="📊",
    layout="wide"
)

# Initialize session state for theme
if 'theme' not in st.session_state:
    st.session_state.theme = 'System Default'

# CSS for a **Modern Animated UI**
animated_css = """
<style>
/* 🎨 Glowing Sidebar with Animation */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a1c24, #0e1117);
    transition: all 0.3s ease-in-out;
    box-shadow: 5px 0px 15px rgba(0, 255, 255, 0.3);
}
[data-testid="stSidebar"] * {
    color: white !important;
}
[data-testid="stSidebar"] .stSelectbox div {
    background-color: #1a1c24 !important;
    color: white !important;
}

/* 🚀 Smooth Font & UI Animation */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
html, body, [class*="st-"] {
    font-family: 'Poppins', sans-serif !important;
}

/* 🌟 3D Floating Effect for Conversion Cards */
.conversion-card {
    background: linear-gradient(145deg, #1a1c24, #0e1117);
    color: white !important;
    border-radius: 12px;
    padding: 20px;
    margin-top: 20px;
    border: 1px solid #00ffff;
    box-shadow: 5px 5px 15px rgba(0, 255, 255, 0.3);
    transition: transform 0.3s ease-in-out;
}
.conversion-card:hover {
    transform: translateY(-5px);
}

/* 🎭 Gradient Buttons with Hover Effect */
.stButton>button {
    background: linear-gradient(to right, #ff7f0e, #ff007f);
    border: none;
    color: white;
    font-size: 18px;
    padding: 12px 24px;
    border-radius: 10px;
    transition: all 0.3s ease-in-out;
}
.stButton>button:hover {
    background: linear-gradient(to right, #ff007f, #ff7f0e);
    transform: scale(1.05);
}

/* 🌟 Glowing Footer Animation */
@keyframes glow {
    0% { text-shadow: 0 0 5px #00ffff; }
    50% { text-shadow: 0 0 20px #00ffff; }
    100% { text-shadow: 0 0 5px #00ffff; }
}
.footer {
    text-align: center;
    padding: 10px;
    color: #00ffff;
    font-size: 18px;
    animation: glow 1.5s infinite alternate;
}
</style>
"""

# Apply custom CSS
st.markdown(animated_css, unsafe_allow_html=True)

# 🎯 **Main App Title with Styling**
st.title("🔥 Ultimate Unit Converter")
st.markdown("### ⚡ Real-time Conversion | 15+ Categories | 100+ Units")

# 🎨 Sidebar with Theme Selector
with st.sidebar:
    st.header("🌟 Features & Settings")
    st.session_state.theme = st.selectbox(
        "🎨 Theme Selector",
        ["Dark", "Light", "System Default"],
        index=["Dark", "Light", "System Default"].index(st.session_state.theme)
    )
    
    st.markdown("""
    - 🚀 **15+ Conversion Categories**
    - 📊 **100+ Supported Units**
    - ⚡ **Real-time Updates**
    - 🧑‍🔬 **Scientific Precision**
    - 📱 **Mobile Friendly**
    """)
    st.markdown("---")
    st.markdown("<div class='footer'>💙 Made with ❤️ by <b>Muhammad Saad</b> using Streamlit</div>", unsafe_allow_html=True)

# 🌟 Unit conversion data (same as before)
unit_conversions = {
    'Length': {'meters': 1, 'kilometers': 1000, 'centimeters': 0.01, 'millimeters': 0.001, 'miles': 1609.34},
    'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
    'Mass': {'grams': 1, 'kilograms': 1000, 'milligrams': 0.001, 'pounds': 453.592, 'ounces': 28.3495},
    'Time': {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400, 'years': 31536000},
    'Speed': {'meters per second': 1, 'kilometers per hour': 0.277778, 'miles per hour': 0.44704, 'knots': 0.514444}
}

# 🌡️ **Temperature Conversion Logic**
def convert_temperature(value, from_unit, to_unit):
    conversion_functions = {
        ('Celsius', 'Fahrenheit'): lambda x: (x * 9/5) + 32,
        ('Celsius', 'Kelvin'): lambda x: x + 273.15,
        ('Fahrenheit', 'Celsius'): lambda x: (x - 32) * 5/9,
        ('Fahrenheit', 'Kelvin'): lambda x: (x - 32) * 5/9 + 273.15,
        ('Kelvin', 'Celsius'): lambda x: x - 273.15,
        ('Kelvin', 'Fahrenheit'): lambda x: (x - 273.15) * 9/5 + 32
    }
    return conversion_functions[(from_unit, to_unit)](value) if from_unit != to_unit else value

# 🎯 **Main UI for Unit Selection & Conversion**
category = st.selectbox("📌 Select Category", list(unit_conversions.keys()))

col1, col2, col3 = st.columns([2,2,3])
with col1:
    from_unit = st.selectbox("From", unit_conversions[category] if category == 'Temperature' else unit_conversions[category].keys())
    
with col2:
    to_unit = st.selectbox("To", unit_conversions[category] if category == 'Temperature' else unit_conversions[category].keys())

with col3:
    value = st.number_input("Enter Value", min_value=0.0, value=1.0, step=0.1, format="%.4f")

# 🔥 **Perform Conversion**
if category == 'Temperature':
    result = convert_temperature(value, from_unit, to_unit)
else:
    result = (value * unit_conversions[category][from_unit]) / unit_conversions[category][to_unit]

# 🎯 **Display Results in a 3D Card**
st.markdown(f"""
<div class="conversion-card">
    <h2 style="text-align:center;">
    🎯 Conversion Result: 
    <span style="color:#ff7f0e">{value:.4f} {from_unit}</span> = 
    <span style="color:#00ffff">{result:.6f} {to_unit}</span>
    </h2>
</div>
""", unsafe_allow_html=True)
