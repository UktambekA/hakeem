import streamlit as st
import streamlit.components.v1 as components

# Sahifa konfiguratsiyasi
st.set_page_config(
    page_title="Tibbiy Manbalar Markazi",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# HTML kodni to'liq kiritamiz
html_code = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
            padding: 30px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        .subtitle {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .search-box {
            margin-bottom: 30px;
            text-align: center;
        }
        
        #searchInput {
            width: 100%;
            max-width: 600px;
            padding: 15px 20px;
            font-size: 16px;
            border: none;
            border-radius: 50px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            outline: none;
        }
        
        .categories {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }
        
        .category {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .category:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
        }
        
        .category-header {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            cursor: pointer;
        }
        
        .category-icon {
            font-size: 2em;
            margin-right: 15px;
        }
        
        .category-title {
            font-size: 1.5em;
            color: #333;
            flex: 1;
        }
        
        .progress-container {
            margin: 10px 0;
        }
        
        .progress-bar {
            width: 100%;
            height: 8px;
            background: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 5px;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
            transition: width 0.3s ease;
        }
        
        .progress-text {
            font-size: 0.85em;
            color: #666;
            text-align: center;
        }
        
        .toggle-btn {
            background: #667eea;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.9em;
            transition: background 0.3s;
            margin-left: 10px;
        }
        
        .toggle-btn:hover {
            background: #764ba2;
        }
        
        .subcategories {
            display: none;
            margin-top: 15px;
        }
        
        .subcategories.active {
            display: block;
        }
        
        .subcategory {
            background: #f8f9fa;
            padding: 12px 15px;
            margin-bottom: 10px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        
        .subcategory-title {
            font-weight: bold;
            color: #667eea;
            margin-bottom: 5px;
        }
        
        .subcategory-content {
            color: #666;
            font-size: 0.95em;
            line-height: 1.6;
        }
        
        .resource-item {
            background: #e8f4f8;
            padding: 8px 12px;
            margin: 5px 0;
            border-radius: 5px;
            font-size: 0.9em;
            display: flex;
            align-items: center;
            cursor: pointer;
            transition: background 0.2s;
        }
        
        .resource-item:hover {
            background: #d0e8f0;
        }
        
        .resource-item.completed {
            background: #d4edda;
        }
        
        .resource-item.completed:hover {
            background: #c3e6cb;
        }
        
        .checkbox {
            margin-right: 10px;
            font-size: 1.2em;
            min-width: 20px;
        }
        
        .resource-text {
            flex: 1;
        }
        
        .resource-item.completed .resource-text {
            text-decoration: line-through;
            color: #666;
        }
        
        .hidden {
            display: none;
        }
        
        .reset-btn {
            background: #dc3545;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 0.9em;
            margin: 20px auto;
            display: block;
            transition: background 0.3s;
        }
        
        .reset-btn:hover {
            background: #c82333;
        }
        
        @media (max-width: 768px) {
            .categories {
                grid-template-columns: 1fr;
            }
            
            h1 {
                font-size: 2em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🏥 Tibbiy Manbalar Markazi</h1>
            <p class="subtitle">Inson anatomiyasi va fiziologiyasi bo'yicha to'liq qo'llanma</p>
        </header>
        
        <div class="search-box">
            <input type="text" id="searchInput" placeholder="Manbalarni qidiring...">
        </div>
        
        <button class="reset-btn" onclick="resetProgress()">🔄 Barcha belgilarni tozalash</button>
        
        <div class="categories" id="categoriesContainer"></div>
    </div>

    <script>
        const data = {
            "Anatomiya (Struktura va Tuzilma)": {
                icon: "🦴",
                subcategories: {
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
                    "Embryologiya": [
                        "Germ layers (ectoderm, mesoderm, endoderm)",
                        "Organogenesis (neural tube, somites)",
                        "Fetal development (trimesters, anomalies)",
                        "Placenta va fetal circulation"
                    ],
                    "Skelet tizimi": [
                        "Axial skeleton (skull, vertebral column, ribs)",
                        "Appendicular skeleton (shoulder, upper/lower limbs)",
                        "Bone histology (osteocytes, Haversian systems)",
                        "Joints (synovial, fibrous, cartilaginous)"
                    ],
                    "Mushak tizimi": [
                        "Head/neck muscles (facial, mastication)",
                        "Trunk muscles (abdominal wall, erector spinae)",
                        "Upper limb (rotator cuff, biceps/triceps)",
                        "Lower limb (gluteals, quadriceps, hamstrings)"
                    ],
                    "Asab tizimi": [
                        "CNS (brain lobes, brainstem, cerebellum, spinal cord)",
                        "PNS (cranial nerves, spinal nerves, dermatomes)",
                        "Autonomic nervous system",
                        "Meninges va CSF circulation"
                    ],
                    "Qon aylanish tizimi": [
                        "Heart (chambers, valves, conduction system)",
                        "Arteries (aorta branches, coronary arteries)",
                        "Veins (vena cava, portal system)",
                        "Lymphatic system (nodes, spleen, thymus)"
                    ],
                    "Nafas tizimi": [
                        "Upper respiratory (nose, pharynx, larynx)",
                        "Lower respiratory (trachea, bronchi, lungs)",
                        "Pleura va mediastinum"
                    ],
                    "Hazm tizimi": [
                        "GI tract (esophagus, stomach, intestines)",
                        "Accessory organs (liver, pancreas, gallbladder)",
                        "Peritoneum (mesentery, omentum)"
                    ],
                    "Siydik chiqarish tizimi": [
                        "Kidneys (nephrons, cortex/medulla)",
                        "Ureters, bladder, urethra"
                    ],
                    "Reproduktiv tizim": [
                        "Male (testes, prostate, seminal vesicles)",
                        "Female (ovaries, uterus, fallopian tubes)"
                    ],
                    "Endokrin tizim": [
                        "Pituitary, thyroid, parathyroid",
                        "Adrenal cortex/medulla",
                        "Pancreas islets, gonads"
                    ],
                    "Teri va integumentary": [
                        "Skin layers (epidermis, dermis, hypodermis)",
                        "Appendages (hair, nails, glands)"
                    ]
                }
            },
            "Fiziologiya (Funksiya va Ishlash)": {
                icon: "⚡",
                subcategories: {
                    "Hujayra fiziologiyasi": [
                        "Membrana potensiali (Na+/K+ pump, action potential)",
                        "Signal transduction (receptors, cAMP, G-proteins)",
                        "Cellular metabolism (glycolysis, Krebs cycle)",
                        "Cell cycle va apoptosis"
                    ],
                    "Homeostaz va regulyatsiya": [
                        "Feedback mechanisms (negative/positive)",
                        "Acid-base balance (buffers, compensation)",
                        "Fluid and electrolyte balance (ADH, aldosterone)"
                    ],
                    "Asab tizimi fiziologiyasi": [
                        "Synaptic transmission (neurotransmitters)",
                        "Sensory physiology (receptors)",
                        "Motor control (reflexes, pyramidal system)",
                        "Higher functions (memory, learning)"
                    ],
                    "Yurak-qon tomir fiziologiyasi": [
                        "Cardiac cycle (systole/diastole, EKG)",
                        "Hemodynamics (blood pressure, Starling's law)",
                        "Vascular physiology (vasoconstriction/dilation)"
                    ],
                    "Nafas fiziologiyasi": [
                        "Ventilation/perfusion matching",
                        "Gas transport (oxygen-hemoglobin curve)",
                        "Respiratory control (chemoreceptors)"
                    ],
                    "Hazm fiziologiyasi": [
                        "Digestion phases (cephalic, gastric, intestinal)",
                        "Enzyme secretion (amylase, pepsin, lipase)",
                        "Nutrient absorption",
                        "Gut hormones (gastrin, CCK, secretin)"
                    ],
                    "Buyrak fiziologiyasi": [
                        "Glomerular filtration (GFR)",
                        "Tubular reabsorption/secretion",
                        "Urine concentration (countercurrent)"
                    ],
                    "Endokrin fiziologiyasi": [
                        "Hormone synthesis (hypothalamus-pituitary axis)",
                        "Insulin/glucagon, thyroid hormones, cortisol",
                        "Endocrine disorders mechanisms"
                    ],
                    "Reproduktiv fiziologiyasi": [
                        "Gonadal hormones (testosterone, estrogen/progesterone)",
                        "Spermatogenesis/oogenesis",
                        "Pregnancy physiology"
                    ],
                    "Immun fiziologiyasi": [
                        "Innate immunity (barriers, complement)",
                        "Adaptive immunity (B/T cells, antibodies)"
                    ],
                    "Mushak fiziologiyasi": [
                        "Excitation-contraction coupling",
                        "Muscle fiber types (slow/fast twitch)",
                        "Fatigue va recovery"
                    ]
                }
            },
            "Patologiya va Kasalliklar": {
                icon: "🔬",
                subcategories: {
                    "Umumiy patologiya": [
                        "Cell injury (reversible/irreversible, hypoxia)",
                        "Inflammation (acute/chronic, mediators)",
                        "Tissue repair (regeneration, fibrosis)",
                        "Neoplasia (benign/malignant, carcinogenesis)"
                    ],
                    "Tizimli patologiya": [
                        "Cardiovascular (atherosclerosis, MI, heart failure)",
                        "Respiratory (pneumonia, COPD, lung cancer)",
                        "Gastrointestinal (ulcers, IBD, cirrhosis)",
                        "Renal (glomerulonephritis, kidney disease)",
                        "Endocrine (diabetes, thyroid disorders)",
                        "Nervous (Alzheimer's, Parkinson's, stroke)",
                        "Musculoskeletal (osteoporosis, arthritis)",
                        "Hematologic (anemia, leukemias)",
                        "Skin (dermatitis, melanoma, psoriasis)"
                    ],
                    "Genetic pathology": [
                        "Trisomies, monogenic disorders"
                    ],
                    "Infectious pathology": [
                        "Bacterial (sepsis), Viral (HIV), Fungal/parasitic"
                    ]
                }
            },
            "Genetika va Molekulyar Biologiya": {
                icon: "🧬",
                subcategories: {
                    "Genetik asoslar": [
                        "DNA structure/replication (double helix, telomeres)",
                        "Gene expression (transcription, translation)",
                        "Mutations (point, frameshift, chromosomal)"
                    ],
                    "Mendelian genetics": [
                        "Inheritance patterns (autosomal, X-linked)"
                    ],
                    "Population genetics": [
                        "Hardy-Weinberg, genetic drift, selection"
                    ],
                    "Epigenetics": [
                        "DNA methylation, histone modification"
                    ],
                    "Genomics": [
                        "NGS, CRISPR editing, pharmacogenomics"
                    ],
                    "Molecular diagnostics": [
                        "PCR variants, gene therapy, stem cells"
                    ]
                }
            },
            "Biokimyo": {
                icon: "⚗️",
                subcategories: {
                    "Biomolecules": [
                        "Carbohydrates (monosaccharides, glycogen)",
                        "Lipids (fatty acids, cholesterol, lipoproteins)",
                        "Proteins (amino acids, folding)",
                        "Nucleic acids (purines/pyrimidines, DNA repair)"
                    ],
                    "Metabolizm": [
                        "Glycolysis/gluconeogenesis",
                        "Citric acid cycle, oxidative phosphorylation",
                        "Fatty acid oxidation/synthesis",
                        "Amino acid metabolism (urea cycle)",
                        "Nucleotide metabolism"
                    ],
                    "Enzymes and vitamins": [
                        "Kinetics (Michaelis-Menten)",
                        "Coenzymes (B vitamins)"
                    ],
                    "Integration": [
                        "Fed/fasted states, metabolic disorders"
                    ]
                }
            },
            "Immunologiya va Mikrobiologiya": {
                icon: "🦠",
                subcategories: {
                    "Immunologiya": [
                        "Innate immunity (barriers, phagocytes, complement)",
                        "Adaptive immunity (MHC, T/B cell activation)",
                        "Antibodies (Ig types, class switching)",
                        "Cytokines (IL-1, TNF, interferons)",
                        "Hypersensitivity reactions (types I-IV)",
                        "Autoimmunity (SLE mechanisms)",
                        "Transplantation immunology",
                        "Vaccines va immunization"
                    ],
                    "Mikrobiologiya": [
                        "Bacterial structure (Gram-positive/negative)",
                        "Viral replication (DNA/RNA viruses)",
                        "Fungal and parasitic infections",
                        "Pathogenesis (toxins, virulence factors)",
                        "Antimicrobial resistance (MRSA)",
                        "Diagnostic methods (culture, PCR, serology)",
                        "Microbiome va dysbiosis"
                    ]
                }
            },
            "Nevrologiya va Psixologiya": {
                icon: "🧠",
                subcategories: {
                    "Nevrologiya": [
                        "Brain structure (cortex, basal ganglia, limbic)",
                        "Neurotransmission (synapses, receptors)",
                        "Sensory systems (vision, audition)",
                        "Motor systems (corticospinal tract, cerebellum)",
                        "Neuroplasticity",
                        "Neuroimaging (fMRI, EEG, PET)"
                    ],
                    "Psixologiya": [
                        "Cognitive processes (attention, memory)",
                        "Emotion and motivation (amygdala, dopamine)",
                        "Behavioral neuroscience (addiction, stress)",
                        "Developmental psychology (Piaget, attachment)",
                        "Mental disorders (schizophrenia, depression)",
                        "Neuropsychology (aphasia types)"
                    ]
                }
            },
            "Amaliy va Klinik Ilm": {
                icon: "🏥",
                subcategories: {
                    "Diagnostika": [
                        "Imaging (X-ray, ultrasound, CT/MRI)",
                        "Lab tests (biopsies, blood analysis)",
                        "Physical examination"
                    ],
                    "Jarrohlik anatomiya": [
                        "Surgical approaches (laparotomy, thoracotomy)",
                        "Vascular anatomy for surgery",
                        "Regional anesthesia (nerve blocks)"
                    ],
                    "Farmakologiya": [
                        "Drug absorption/distribution",
                        "Pharmacodynamics (agonists/antagonists)",
                        "Adverse effects"
                    ],
                    "Epidemiologiya": [
                        "Disease incidence/prevalence",
                        "Risk factors"
                    ],
                    "Reabilitatsiya": [
                        "Physiotherapy for recovery"
                    ]
                }
            },
            "Evolyutsiya va Ekologiya": {
                icon: "🌍",
                subcategories: {
                    "Evolyutsion biologiya": [
                        "Human origins (Homo sapiens migration)",
                        "Adaptive traits (bipedalism, brain size)",
                        "Genetic evolution",
                        "Comparative anatomy"
                    ],
                    "Ekologik ta'sir": [
                        "Environmental adaptations (altitude, pigmentation)",
                        "Pollution effects",
                        "Climate change impacts",
                        "Microbiome ecology"
                    ],
                    "Evolyutsion tibbiyot": [
                        "Mismatch diseases (obesity)",
                        "Zoonotic diseases (COVID origins)"
                    ]
                }
            }
        };

        // LocalStorage dan ma'lumotlarni yuklash
        function loadProgress() {
            const saved = localStorage.getItem('medicalProgress');
            return saved ? JSON.parse(saved) : {};
        }

        // LocalStorage ga saqlash
        function saveProgress(progress) {
            localStorage.setItem('medicalProgress', JSON.stringify(progress));
        }

        let progress = loadProgress();

        function calculateProgress(categoryName) {
            const category = data[categoryName];
            let total = 0;
            let completed = 0;

            Object.entries(category.subcategories).forEach(([subcat, items]) => {
                items.forEach((item, index) => {
                    total++;
                    const key = `${categoryName}|||${subcat}|||${index}`;
                    if (progress[key]) completed++;
                });
            });

            return { completed, total, percentage: total > 0 ? Math.round((completed / total) * 100) : 0 };
        }

        function toggleItem(categoryName, subcatName, index) {
            const key = `${categoryName}|||${subcatName}|||${index}`;
            progress[key] = !progress[key];
            saveProgress(progress);
            renderCategories();
        }

        function resetProgress() {
            if (confirm('Barcha belgilarni o\\'chirishni xohlaysizmi?')) {
                progress = {};
                saveProgress(progress);
                renderCategories();
            }
        }

        function renderCategories() {
            const container = document.getElementById('categoriesContainer');
            container.innerHTML = '';
            
            Object.entries(data).forEach(([category, content]) => {
                const categoryDiv = document.createElement('div');
                categoryDiv.className = 'category';
                
                const stats = calculateProgress(category);
                
                let subcategoriesHTML = '';
                Object.entries(content.subcategories).forEach(([subcat, items]) => {
                    const itemsHTML = items.map((item, index) => {
                        const key = `${category}|||${subcat}|||${index}`;
                        const isCompleted = progress[key];
                        return `
                            <div class="resource-item ${isCompleted ? 'completed' : ''}" 
                                 onclick="toggleItem('${category}', '${subcat}', ${index})">
                                <span class="checkbox">${isCompleted ? '✅' : '⬜'}</span>
                                <span class="resource-text">${item}</span>
                            </div>
                        `;
                    }).join('');
                    
                    subcategoriesHTML += `
                        <div class="subcategory">
                            <div class="subcategory-title">${subcat}</div>
                            <div class="subcategory-content">${itemsHTML}</div>
                        </div>
                    `;
                });
                
                categoryDiv.innerHTML = `
                    <div class="category-header" onclick="toggleCategory(this)">
                        <span class="category-icon">${content.icon}</span>
                        <h2 class="category-title">${category}</h2>
                        <button class="toggle-btn">Ko'rish</button>
                    </div>
                    <div class="progress-container">
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: ${stats.percentage}%"></div>
                        </div>
                        <div class="progress-text">${stats.completed}/${stats.total} tugallandi (${stats.percentage}%)</div>
                    </div>
                    <div class="subcategories">
                        ${subcategoriesHTML}
                    </div>
                `;
                
                container.appendChild(categoryDiv);
            });
        }

        function toggleCategory(header) {
            const subcategories = header.parentElement.querySelector('.subcategories');
            const btn = header.querySelector('.toggle-btn');
            
            subcategories.classList.toggle('active');
            btn.textContent = subcategories.classList.contains('active') ? 'Yopish' : 'Ko\\'rish';
        }

        document.getElementById('searchInput').addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            const categories = document.querySelectorAll('.category');
            
            categories.forEach(category => {
                const text = category.textContent.toLowerCase();
                if (text.includes(searchTerm)) {
                    category.classList.remove('hidden');
                } else {
                    category.classList.add('hidden');
                }
            });
        });

        renderCategories();
    </script>
</body>
</html>
"""

# HTML komponentni ko'rsatish
components.html(html_code, height=900, scrolling=True)
