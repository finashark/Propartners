import streamlit as st
import datetime
from typing import Dict, Any
from content import CONTENT

# Initialize session state for language
if "language" not in st.session_state:
    st.session_state.language = "en"  # Default to English

# Page configuration
st.set_page_config(
    page_title=CONTENT[st.session_state.language]["page_title"],
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS
def load_css():
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Reset and Base Styles */
    .stApp {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom navbar */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid #e5e7eb;
        padding: 1rem 0;
    }
    
    .navbar-content {
        max-width: 1280px;
        margin: 0 auto;
        padding: 0 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .navbar-right {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .logo {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .logo-icon {
        width: 36px;
        height: 36px;
        background: black;
        color: white;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
    }
    
    .nav-links {
        display: flex;
        gap: 1.5rem;
        font-size: 0.875rem;
    }
    
    .nav-links a {
        color: #6b7280;
        text-decoration: none;
        transition: color 0.2s;
    }
    
    .nav-links a:hover {
        color: black;
    }
    
    .cta-button {
        background: black;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 1rem;
        text-decoration: none;
        font-size: 0.875rem;
        font-weight: 500;
        transition: background-color 0.2s;
    }
    
    .cta-button:hover {
        background: #374151;
        color: white;
    }
    
    /* Language switcher */
    .lang-switcher {
        display: flex;
        align-items: center;
        gap: 0.25rem;
        padding: 0.25rem 0.5rem;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        background: white;
        cursor: pointer;
        transition: all 0.2s;
        font-size: 0.875rem;
    }
    
    .lang-switcher:hover {
        border-color: #d1d5db;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .lang-flag {
        font-size: 1rem;
    }
    
    .lang-code {
        font-weight: 500;
        text-transform: uppercase;
        font-size: 0.75rem;
    }
    
    /* Add top padding to account for fixed navbar */
    .main-content {
        padding-top: 80px;
    }
    
    /* Hero section */
    .hero-section {
        background: linear-gradient(135deg, #f9fafb 0%, #ffffff 50%, #f3f4f6 100%);
        background-image: 
            radial-gradient(circle at 20% 20%, rgba(59, 130, 246, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(16, 185, 129, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 60%, rgba(139, 92, 246, 0.05) 0%, transparent 50%);
        padding: 5rem 0;
        margin: 0 -1rem;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23000000' fill-opacity='0.02'%3E%3Ccircle cx='30' cy='30' r='2'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E") repeat;
        pointer-events: none;
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: bold;
        line-height: 1.1;
        margin-bottom: 1.25rem;
    }
    
    .hero-subtitle {
        font-size: 1.125rem;
        color: #6b7280;
        margin-bottom: 1.5rem;
    }
    
    .hero-buttons {
        display: flex;
        gap: 0.75rem;
        flex-wrap: wrap;
        margin-bottom: 1rem;
    }
    
    .btn-primary {
        background: black;
        color: white;
        padding: 0.75rem 1.25rem;
        border-radius: 1rem;
        text-decoration: none;
        font-size: 0.875rem;
        font-weight: 500;
        border: none;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    
    .btn-secondary {
        background: white;
        color: black;
        padding: 0.75rem 1.25rem;
        border-radius: 1rem;
        text-decoration: none;
        font-size: 0.875rem;
        font-weight: 500;
        border: 1px solid #d1d5db;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    
    .btn-primary:hover {
        background: #374151;
    }
    
    .btn-secondary:hover {
        background: #f9fafb;
    }
    
    /* Card styles */
    .service-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 1.5rem;
        padding: 2rem;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .service-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    
    .service-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border-color: #d1d5db;
    }
    
    .service-card:hover::before {
        transform: scaleX(1);
    }
    
    .service-icon {
        width: 48px;
        height: 48px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .service-card h3 {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
        color: #111827;
    }
    
    .service-card p {
        font-size: 0.875rem;
        color: #6b7280;
        margin-bottom: 1.5rem;
        line-height: 1.6;
    }
    
    .service-card ul {
        list-style: none;
        padding: 0;
    }
    
    .service-card li {
        font-size: 0.875rem;
        display: flex;
        align-items: flex-start;
        gap: 0.75rem;
        margin-bottom: 0.5rem;
        color: #374151;
    }
    
    .service-card li::before {
        content: "✓";
        color: #10b981;
        font-weight: bold;
        margin-top: 0.125rem;
        width: 16px;
        height: 16px;
        border-radius: 50%;
        background: #ecfdf5;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75rem;
        flex-shrink: 0;
    }
    
    /* Section styles */
    .section {
        padding: 5rem 0;
        position: relative;
    }
    
    .section-alt {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        margin: 0 -1rem;
        padding: 5rem 1rem;
        position: relative;
        overflow: hidden;
    }
    
    .section-alt::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23000000' fill-opacity='0.02'%3E%3Cpath d='M30 30c0-16.569 13.431-30 30-30s30 13.431 30 30-13.431 30-30 30-30-13.431-30-30zm30-20c-11.046 0-20 8.954-20 20s8.954 20 20 20 20-8.954 20-20-8.954-20-20-20z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E") repeat;
        pointer-events: none;
    }
    
    .section-dark {
        background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
        color: white;
        margin: 0 -1rem;
        padding: 5rem 1rem;
        position: relative;
        overflow: hidden;
    }
    
    .section-dark::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M20 20c0-11.046 8.954-20 20-20s20 8.954 20 20-8.954 20-20 20-20-8.954-20-20z'/%3E%3C/g%3E%3C/svg%3E") repeat;
        pointer-events: none;
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .section-subtitle {
        color: #6b7280;
        margin-bottom: 2rem;
    }
    
    .section-dark .section-subtitle {
        color: #d1d5db;
    }
    
    /* Stats cards */
    .stats-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 1rem;
        padding: 1.25rem;
        text-align: center;
    }
    
    .stats-number {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.25rem;
    }
    
    .stats-label {
        font-size: 0.875rem;
        color: #6b7280;
    }
    
    /* Trust section */
    .trust-logos {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 1.5rem;
        opacity: 0.8;
    }
    
    .trust-logo {
        height: 80px;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.875rem;
        color: #6b7280;
        background: white;
        transition: all 0.3s ease;
        padding: 1rem;
        position: relative;
        overflow: hidden;
    }
    
    .trust-logo:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border-color: #d1d5db;
    }
    
    .trust-logo img {
        max-width: 120px;
        max-height: 40px;
        object-fit: contain;
        filter: grayscale(1) opacity(0.7);
        transition: filter 0.3s ease;
    }
    
    .trust-logo:hover img {
        filter: grayscale(0) opacity(1);
    }
    
    /* Brand logo styles */
    .brand-logo {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        font-size: 0.75rem;
        letter-spacing: 0.05em;
    }
    
    .fintech-logo {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .retail-logo {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    .tech-logo {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    
    .hfm-logo {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        font-weight: bold;
        border: 2px solid #10b981;
    }
    
    /* Form styles */
    .contact-form {
        background: white;
        border-radius: 1.5rem;
        padding: 1.5rem;
        border: 1px solid #e5e7eb;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .navbar-content {
            padding: 0 1rem;
        }
        
        .nav-links {
            display: none;
        }
        
        .hero-title {
            font-size: 2rem;
        }
        
        .section-title {
            font-size: 1.5rem;
        }
    }
    
    /* Custom streamlit styling */
    .stButton > button {
        width: 100%;
        border-radius: 1rem;
        border: none;
        background: black;
        color: white;
        font-weight: 500;
        padding: 0.75rem 1.25rem;
        transition: background-color 0.2s;
    }
    
    .stButton > button:hover {
        background: #374151;
    }
    
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        border-radius: 0.75rem;
        border: 1px solid #d1d5db;
    }
    
    /* Case study cards */
    .case-card {
        border-radius: 1.5rem;
        overflow: hidden;
        border: 1px solid #e5e7eb;
        background: white;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .case-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    
    .case-image {
        height: 200px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        position: relative;
        overflow: hidden;
    }
    
    .case-image.fintech {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .case-image.edtech {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    .case-image.ecommerce {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    
    .case-image::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23ffffff' fill-opacity='0.1'%3E%3Cpath d='M20 20c0-8.837 7.163-16 16-16s16 7.163 16 16-7.163 16-16 16-16-7.163-16-16zm16-8c-4.418 0-8 3.582-8 8s3.582 8 8 8 8-3.582 8-8-3.582-8-8-8z'/%3E%3C/g%3E%3C/svg%3E") repeat;
    }
    
    .case-overlay {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        color: white;
    }
    
    .case-icon {
        font-size: 3rem;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .case-label {
        font-size: 0.875rem;
        font-weight: 600;
        opacity: 0.9;
    }
    
    /* Network visualization */
    .network-viz {
        position: relative;
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border-radius: 1.5rem;
        padding: 2rem;
        min-height: 300px;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }
    
    .network-viz::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23000000' fill-opacity='0.03'%3E%3Ccircle cx='50' cy='50' r='4'/%3E%3Ccircle cx='25' cy='25' r='2'/%3E%3Ccircle cx='75' cy='25' r='2'/%3E%3Ccircle cx='25' cy='75' r='2'/%3E%3Ccircle cx='75' cy='75' r='2'/%3E%3Cline x1='50' y1='50' x2='25' y2='25' stroke='%23000000' stroke-opacity='0.02' stroke-width='1'/%3E%3Cline x1='50' y1='50' x2='75' y2='25' stroke='%23000000' stroke-opacity='0.02' stroke-width='1'/%3E%3Cline x1='50' y1='50' x2='25' y2='75' stroke='%23000000' stroke-opacity='0.02' stroke-width='1'/%3E%3Cline x1='50' y1='50' x2='75' y2='75' stroke='%23000000' stroke-opacity='0.02' stroke-width='1'/%3E%3C/g%3E%3C/svg%3E") repeat;
        pointer-events: none;
    }
    
    </style>
    """, unsafe_allow_html=True)

def render_navbar():
    content = CONTENT[st.session_state.language]
    navbar = content["navbar"]
    
    # Language switcher in sidebar
    with st.container():
        col1, col2, col3 = st.columns([1, 6, 1])
        
        with col3:
            # Language switcher
            current_lang = st.session_state.language
            if current_lang == "en":
                flag = "🇺🇸"
                lang_name = "EN"
                other_lang = "vi"
                other_flag = "🇻🇳"
                other_name = "VI"
            else:
                flag = "🇻🇳"
                lang_name = "VI"
                other_lang = "en"
                other_flag = "🇺🇸"
                other_name = "EN"
            
            if st.button(f"{other_flag} {other_name}", key="lang_switch", help="Switch language"):
                st.session_state.language = other_lang
                st.rerun()
    
    # Navbar HTML
    st.markdown(f"""
    <div class="navbar">
        <div class="navbar-content">
            <div class="logo">
                <div class="logo-icon">PP</div>
                <div style="font-weight: 600;">ProPartners</div>
                <span style="font-size: 0.875rem; color: #6b7280; margin-left: 0.5rem;">{navbar["tagline"]}</span>
            </div>
            <nav class="nav-links">
                <a href="#services">{navbar["services"]}</a>
                <a href="#why">{navbar["why_us"]}</a>
                <a href="#regions">{navbar["regions"]}</a>
                <a href="#process">{navbar["process"]}</a>
                <a href="#cases">{navbar["cases"]}</a>
                <a href="#compliance">{navbar["compliance"]}</a>
                <a href="#contact">{navbar["contact"]}</a>
            </nav>
            <div class="navbar-right">
                <div class="lang-switcher" onclick="window.dispatchEvent(new Event('langswitch'))">
                    <span class="lang-flag">{flag}</span>
                    <span class="lang-code">{lang_name}</span>
                </div>
                <a href="#contact" class="cta-button">{navbar["cta"]}</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_hero():
    content = CONTENT[st.session_state.language]
    hero = content["hero"]
    
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown(f"""
        <h1 class="hero-title">
            {hero["title"]}
        </h1>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <p class="hero-subtitle">
            {hero["subtitle"]}
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="hero-buttons">
            <a href="#contact" class="btn-primary">{hero["cta_primary"]}</a>
            <a href="#services" class="btn-secondary">{hero["cta_secondary"]}</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <p style="font-size: 0.75rem; color: #6b7280;">
            {hero["disclaimer"]}
        </p>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="position: relative;">
            <div class="network-viz">
                <div style="text-align: center; position: relative; z-index: 2;">
                    <div style="font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.05em; color: #6b7280; margin-bottom: 1rem;">{hero["network_title"]}</div>
                    <div style="font-size: 2.5rem; font-weight: 700; margin-bottom: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">{hero["network_stats"]}</div>
                    <div style="color: #6b7280; font-weight: 500;">{hero["network_desc"]}</div>
                    <div style="margin-top: 1.5rem; display: flex; justify-content: center; gap: 1rem;">
                        <div style="width: 12px; height: 12px; border-radius: 50%; background: #667eea;"></div>
                        <div style="width: 8px; height: 8px; border-radius: 50%; background: #764ba2; margin-top: 2px;"></div>
                        <div style="width: 10px; height: 10px; border-radius: 50%; background: #10b981; margin-top: 1px;"></div>
                        <div style="width: 6px; height: 6px; border-radius: 50%; background: #f59e0b; margin-top: 3px;"></div>
                    </div>
                </div>
            </div>
            <div style="position: absolute; bottom: -24px; right: -24px; border-radius: 1.5rem; background: white; box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15); border: 1px solid #e5e7eb; padding: 1.5rem; width: 20rem; backdrop-filter: blur(10px);">
                <div style="font-size: 0.75rem; color: #6b7280; margin-bottom: 1rem; font-weight: 500;">{hero["kpi_title"]}</div>
                <div style="display: flex; justify-content: space-between; align-items: end;">
                    <div>
                        <div style="font-size: 1.75rem; font-weight: bold; background: linear-gradient(135deg, #10b981 0%, #059669 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">+142%</div>
                        <div style="font-size: 0.75rem; color: #6b7280; margin-top: 0.25rem;">{hero["kpi_mrr"]}</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 1.75rem; font-weight: bold; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">28 {hero["kpi_launch"].split()[-1] if len(hero["kpi_launch"].split()) > 1 else "days"}</div>
                        <div style="font-size: 0.75rem; color: #6b7280; margin-top: 0.25rem;">{hero["kpi_launch"]}</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_trust_section():
    content = CONTENT[st.session_state.language]
    trust = content["trust"]
    
    # Define partner brands
    partners = [
        {"name": "HFM", "class": "hfm-logo", "type": "Forex & CFD"},
        {"name": "MetaTrader", "class": "fintech-logo", "type": "Trading Platform"},
        {"name": "TradingView", "class": "tech-logo", "type": "Market Analysis"},
        {"name": "Shopee", "class": "retail-logo", "type": "E-commerce SEA"},
        {"name": "Grab", "class": "tech-logo", "type": "Super App"},
        {"name": "Binance", "class": "fintech-logo", "type": "Crypto Exchange"},
        {"name": "Visa", "class": "fintech-logo", "type": "Payment Network"},
        {"name": "Mastercard", "class": "fintech-logo", "type": "Payment Solutions"},
        {"name": "PayPal", "class": "fintech-logo", "type": "Digital Payments"},
    ]
    
    st.markdown(f"""
    <div class="section">
        <div style="text-align: center; font-size: 0.875rem; color: #6b7280; margin-bottom: 2rem;">
            {trust["title"]}
        </div>
        <div class="trust-logos">
    """, unsafe_allow_html=True)
    
    cols = st.columns(3)
    for i, partner in enumerate(partners):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="trust-logo brand-logo {partner['class']}">
                <div style="text-align: center;">
                    <div style="font-size: 0.875rem; font-weight: 600; margin-bottom: 0.25rem;">{partner['name']}</div>
                    <div style="font-size: 0.625rem; opacity: 0.8;">{partner['type']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

def render_services():
    content = CONTENT[st.session_state.language]
    services_content = content["services"]
    
    st.markdown('<div id="services" class="section-alt">', unsafe_allow_html=True)
    
    st.markdown(f"""
    <h2 class="section-title">{services_content["title"]}</h2>
    <p class="section-subtitle">{services_content["subtitle"]}</p>
    """, unsafe_allow_html=True)
    
    services = services_content["items"]
    
    # Service icons mapping
    service_icons = ["🤝", "📱", "🎯", "🚀", "⚙️", "🎨"]
    
    cols = st.columns(3)
    for idx, service in enumerate(services):
        with cols[idx % 3]:
            bullets_html = "".join([f"<li>{bullet}</li>" for bullet in service["bullets"]])
            st.markdown(f"""
            <div class="service-card">
                <div class="service-icon">{service_icons[idx]}</div>
                <h3>{service["title"]}</h3>
                <p>{service["desc"]}</p>
                <ul>
                    {bullets_html}
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_why_us():
    content = CONTENT[st.session_state.language]
    why_us = content["why_us"]
    
    st.markdown('<div id="why" class="section">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"""
        <h2 class="section-title">{why_us["title"]}</h2>
        <p class="section-subtitle">{why_us["subtitle"]}</p>
        """, unsafe_allow_html=True)
        
        reasons = why_us["reasons"]
        
        sub_cols = st.columns(2)
        for idx, reason in enumerate(reasons):
            with sub_cols[idx % 2]:
                # Add icons for each reason
                reason_icons = ["⚖️", "🌏", "📋", "⚡"]
                st.markdown(f"""
                <div style="border: 1px solid #e5e7eb; border-radius: 1.5rem; padding: 1.5rem; margin-bottom: 1rem; background: white; transition: all 0.3s ease; position: relative; overflow: hidden;" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 10px 25px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">{reason_icons[idx]}</div>
                    <div style="font-weight: 600; margin-bottom: 0.5rem; color: #111827;">{reason[0]}</div>
                    <div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">{reason[1]}</div>
                </div>
                """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="border-radius: 1.5rem; border: 1px solid #e5e7eb; padding: 1.5rem; background: #f9fafb;">
            <div style="font-size: 0.875rem; color: #6b7280;">{why_us["stats_title"]}</div>
        """, unsafe_allow_html=True)
        
        kpis = why_us["stats"]
        
        kpi_cols = st.columns(2)
        for idx, kpi in enumerate(kpis):
            with kpi_cols[idx % 2]:
                st.markdown(f"""
                <div class="stats-card" style="margin-bottom: 1rem;">
                    <div class="stats-number">{kpi[0]}</div>
                    <div class="stats-label">{kpi[1]}</div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_regions():
    content = CONTENT[st.session_state.language]
    regions_content = content["regions"]
    
    st.markdown('<div id="regions" class="section-alt">', unsafe_allow_html=True)
    
    st.markdown(f"""
    <h2 class="section-title">{regions_content["title"]}</h2>
    <p class="section-subtitle">{regions_content["subtitle"]}</p>
    """, unsafe_allow_html=True)
    
    regions = regions_content["items"]
    
    cols = st.columns(3)
    for idx, region in enumerate(regions):
        with cols[idx]:
            st.markdown(f"""
            <div class="service-card">
                <h3>{region[0]}</h3>
                <p>{region[1]}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_process():
    content = CONTENT[st.session_state.language]
    process_content = content["process"]
    
    st.markdown('<div id="process" class="section">', unsafe_allow_html=True)
    
    st.markdown(f"""
    <h2 class="section-title">{process_content["title"]}</h2>
    """, unsafe_allow_html=True)
    
    steps = process_content["steps"]
    
    cols = st.columns(4)
    step_icons = ["🔍", "📊", "🚀", "📈"]
    for idx, step in enumerate(steps):
        with cols[idx]:
            st.markdown(f"""
            <div style="border: 1px solid #e5e7eb; border-radius: 1.5rem; padding: 2rem 1.5rem; background: white; position: relative; text-align: center; transition: all 0.3s ease;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
                <div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); width: 30px; height: 30px; border-radius: 50%; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 0.875rem;">{idx+1}</div>
                <div style="font-size: 2rem; margin: 1rem 0 1rem 0;">{step_icons[idx]}</div>
                <div style="font-weight: 600; margin-bottom: 0.5rem; color: #111827;">Bước {idx+1}</div>
                <div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">{step}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_cases():
    content = CONTENT[st.session_state.language]
    cases_content = content["cases"]
    
    st.markdown('<div id="cases" class="section-alt">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
        <h2 class="section-title">{cases_content["title"]}</h2>
        <p class="section-subtitle">{cases_content["subtitle"]}</p>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <a href="#contact" style="display: inline-flex; border-radius: 1rem; padding: 0.5rem 1rem; border: 1px solid #e5e7eb; font-size: 0.875rem; text-decoration: none; color: black;">{cases_content["cta"]}</a>
        """, unsafe_allow_html=True)
    
    cases = cases_content["items"]
    
    # Case study icons and classes
    case_data = [
        {"icon": "💰", "class": "fintech"},
        {"icon": "📚", "class": "edtech"}, 
        {"icon": "🛒", "class": "ecommerce"}
    ]
    
    cols = st.columns(3)
    for idx, case in enumerate(cases):
        with cols[idx]:
            case_info = case_data[idx]
            st.markdown(f"""
            <article class="case-card">
                <div class="case-image {case_info['class']}">
                    <div class="case-overlay">
                        <span class="case-icon">{case_info['icon']}</span>
                        <div class="case-label">{case[0]}</div>
                    </div>
                </div>
                <div style="padding: 1.5rem;">
                    <h3 style="font-weight: 600; margin-bottom: 0.5rem; font-size: 1.125rem;">{case[0]}</h3>
                    <p style="font-size: 0.875rem; color: #6b7280; margin-bottom: 0.5rem; font-weight: 600;">{case[1]}</p>
                    <p style="font-size: 0.75rem; color: #9ca3af;">
                        <span style="background: #f3f4f6; padding: 0.25rem 0.5rem; border-radius: 0.375rem; font-weight: 500;">
                            {case[2]}
                        </span>
                    </p>
                </div>
            </article>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_compliance():
    content = CONTENT[st.session_state.language]
    compliance_content = content["compliance"]
    
    st.markdown('<div id="compliance" class="section">', unsafe_allow_html=True)
    
    st.markdown(f"""
    <h2 class="section-title">{compliance_content["title"]}</h2>
    """, unsafe_allow_html=True)
    
    compliance_items = compliance_content["items"]
    
    cols = st.columns(3)
    for idx, item in enumerate(compliance_items):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="service-card">
                <h3>{item[0]}</h3>
                <p>{item[1]}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_contact_form():
    content = CONTENT[st.session_state.language]
    contact = content["contact"]
    
    st.markdown('<div id="contact" class="section-dark">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"""
        <h2 style="font-size: 2rem; font-weight: bold; margin-bottom: 0.5rem; color: white;">{contact["title"]}</h2>
        <p style="color: #d1d5db; margin-bottom: 1.5rem;">{contact["subtitle"]}</p>
        <ul style="color: #d1d5db; font-size: 0.875rem; list-style: none; padding: 0;">
        """, unsafe_allow_html=True)
        
        for feature in contact["features"]:
            st.markdown(f"""
            <li style="margin-bottom: 0.5rem;">• {feature}</li>
            """, unsafe_allow_html=True)
        
        st.markdown("</ul>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="contact-form">', unsafe_allow_html=True)
        
        form = contact["form"]
        
        with st.form("contact_form"):
            company = st.text_input(form["company"], placeholder=form["company_placeholder"])
            
            col_name, col_email = st.columns(2)
            with col_name:
                name = st.text_input(form["name"], placeholder=form["name_placeholder"])
            with col_email:
                email = st.text_input(form["email"], placeholder=form["email_placeholder"])
            
            region = st.selectbox(
                form["region"],
                form["region_options"]
            )
            
            objectives = st.text_area(
                form["objectives"],
                placeholder=form["objectives_placeholder"],
                height=100
            )
            
            submitted = st.form_submit_button(form["submit"])
            
            if submitted:
                if company and name and email and objectives:
                    # Here you would normally process the form data
                    st.success(form["success"])
                    # You could integrate with email service, database, etc.
                else:
                    st.error(form["error"])
        
        st.markdown(f"""
        <p style="font-size: 0.75rem; color: #6b7280; text-align: center; margin-top: 1rem;">
            {form["privacy"]}
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_footer():
    content = CONTENT[st.session_state.language]
    footer = content["footer"]
    current_year = datetime.datetime.now().year
    
    st.markdown(f"""
    <footer style="border-top: 1px solid #e5e7eb; padding: 2rem 0; font-size: 0.875rem; color: #6b7280;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem;">
            <div>© {current_year} {footer["copyright"]}</div>
            <div style="display: flex; gap: 1rem;">
                <a href="#" style="color: #6b7280; text-decoration: none;">{footer["links"][0]}</a>
                <a href="#" style="color: #6b7280; text-decoration: none;">{footer["links"][1]}</a>
                <a href="#" style="color: #6b7280; text-decoration: none;">{footer["links"][2]}</a>
            </div>
        </div>
    </footer>
    """, unsafe_allow_html=True)

def main():
    # Load CSS
    load_css()
    
    # Render navbar
    render_navbar()
    
    # Main content container
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    # Render sections
    render_hero()
    render_trust_section()
    render_services()
    render_why_us()
    render_regions()
    render_process()
    render_cases()
    render_compliance()
    render_contact_form()
    render_footer()
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()