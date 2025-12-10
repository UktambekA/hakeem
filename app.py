import streamlit as st

st.set_page_config(page_title="Tibbiy Manbalar Markazi", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
    }
    .header {
        text-align: center;
        color: white;
        margin-bottom: 40px;
        padding: 30px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    .search-box {
        text-align: center;
        margin-bottom: 30px;
    }
    .category {
        background: white;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    }
    .category-header {
        display: flex;
        align-items: center;
        cursor: pointer;
        user-select: none;
    }
    .category-icon {
        font-size: 2em;
        margin-right: 15px;
    }
    .category-title {
        flex: 1;
        font-size: 1.5em;
        color: #333;
    }
    .toggle-btn {
        background: #667eea;
        color: white;
        border: none;
        padding: 8px 15px;
        border-radius: 20px;
        cursor: pointer;
    }
    .subcategory {
        background: #f8f9fa;
        padding: 12px 15px;
        margin: 10px 0;
        border-radius: 8px;
        border-left: 4px solid #667eea;
    }
    .subcategory-title {
        font-weight: bold;
        color: #667eea;
    }
    .resource-item {
        background: #e8f4f8;
        padding: 8px 12px;
        margin: 5px 0;
        border-radius: 5px;
        font-size: 0.9em;
    }
</style>
""", unsafe_allow_html=True)

# Ma'lumotlar (oldingi JSON ni Python dict ga o'tkazdim)
data = {
    "Anatomiya (Struktura va Tuzilma)": {
        "icon": "🦴",
        "subcategories": {
            "Umumiy anatomiya va terminologiya": [
                "Anatomik pozitsiyalar (sagittal, coronal, transverse planes)",
                "Harakat terminlari (flexion/extension, abduction/adduction)",
                "Tana bo'limlari (thoracic, abdominal, pelvic cavities)",
                "Surface anatomy (McBurney's point va boshqalar)"
            ],
            "Histologiya va to'qimalar": [
                "Epiteliy to'qimasi (simple, stratified, columnar)",
                "Bog'lovchi to'qima (areolar, dense, adipose, cartilage)",
                "Mushak to'qimasi (skeletal, smooth, cardiac)",
                "Nerv to'qimasi (neurons, glial cells)"
            ],
            # ... qolgan submavzular (oldingi HTML dagi barchasini qo'shing)
        }
    },
    # Barcha 9 ta kategoriyani shu yerda to'liq qo'shing (joy tufayli qisqartirdim)
}

# Header
st.markdown("""
<div class="header">
    <h1>🏥 Tibbiy Manbalar Markazi</h1>
    <p class="subtitle">Inson anatomiyasi va fiziologiyasi bo'yicha to'liq qo'llanma</p>
</div>
""", unsafe_allow_html=True)

# Qidiruv
st.markdown('<div class="search-box">', unsafe_allow_html=True)
search_term = st.text_input("", placeholder="Manbalarni qidiring...", key="search")
st.markdown('</div>', unsafe_allow_html=True)

# Kategoriyalarni ko'rsatish
for category, content in data.items():
    text_contains_search = search_term.lower() in category.lower()
    if search_term:
        # Qidiruv bo'lsa, faqat mos keladiganlarni ko'rsat
        subcategory_match = any(search_term.lower() in sub.lower() for sub in content["subcategories"])
        item_match = any(search_term.lower() in " ".join(items).lower() for items in content["subcategories"].values())
        if not (text_contains_search or subcategory_match or item_match):
            continue

    with st.expander(f"{content['icon']} {category}", expanded=False):
        for subcat, items in content["subcategories"].items():
            if search_term and search_term.lower() not in subcat.lower() and not any(search_term.lower() in item.lower() for item in items):
                continue
            st.markdown(f"**{subcat}**")
            for item in items:
                if search_term and search_term.lower() not in item.lower():
                    continue
                st.markdown(f"<div class='resource-item'>{item}</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
