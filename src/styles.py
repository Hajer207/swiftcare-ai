def load_css():
    return """
    <style>

    .stApp {
        background: linear-gradient(135deg, #eef8ff 0%, #f8fcff 100%);
    }

    section[data-testid="stSidebar"] {
        background-color: #d6eefb;
    }

    .main-title {
        font-size: 58px;
        font-weight: 900;
        color: #12344d;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 22px;
        color: #3f6f88;
        margin-bottom: 35px;
        font-weight: 500;
    }

    .card {
        background-color: white;
        padding: 24px;
        border-radius: 18px;
        box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        border-left: 6px solid #7ec8f5;
    }

    .metric-title {
        color: #5b7280;
        font-size: 15px;
        font-weight: 700;
    }

    .metric-value {
        color: #12344d;
        font-size: 30px;
        font-weight: 900;
    }

    .critical-box {
        background-color: #ffe5e5;
        color: #9b111e;
        padding: 18px;
        border-radius: 16px;
        border-left: 8px solid #e63946;
        font-size: 20px;
        font-weight: 800;
        margin-top: 20px;
    }

    .safe-box {
        background-color: #e8f8f1;
        color: #116b4f;
        padding: 18px;
        border-radius: 16px;
        border-left: 8px solid #2ecc71;
        font-size: 18px;
        font-weight: 700;
        margin-top: 20px;
    }

    div.stButton > button {
        width: 100%;
        background-color: #4bb3e6;
        color: white;
        border-radius: 14px;
        border: none;
        padding: 0.8rem;
        font-size: 18px;
        font-weight: 700;
    }

    div.stButton > button:hover {
        background-color: #249bd3;
        color: white;
    }

    </style>
    """