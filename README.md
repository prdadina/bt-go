# BT-GO Asistent Virtual - Instrucțiuni de Setup

## 📋 Prezentare Generală

Acest proiect implementează un asistent virtual inteligent pentru aplicația bancară BT-GO, destinat persoanelor juridice. Asistentul oferă sfaturi financiare personalizate pentru îmbunătățirea EBITDA, rating-ului de credit și gestionarea eficientă a fluxului de numerar.

## 🚀 Instalare și Configurare

### 1. Pregătirea Mediului Python

```bash
# Creează un mediu virtual
python -m venv bt_go_env

# Activează mediul virtual
# Windows:
bt_go_env\Scripts\activate
# macOS/Linux:
source bt_go_env/bin/activate
```

### 2. Instalarea Dependențelor

```bash
# Instalează pachetele necesare
pip install -r requirements.txt
```

### 3. Structura Proiectului

```
bt_go_assistant/
│
├── app.py              # Backend-ul Flask
├── requirements.txt    # Dependențe Python
├── index.html         # Frontend-ul web
└── README.md          # Documentație
```

### 4. Rularea Aplicației

```bash
# Rulează serverul backend
python app.py
```

Serverul va rula pe `http://localhost:5000`

### 5. Testarea Aplicației

1. Deschide `index.html` într-un browser web
2. Click pe butonul asistentului virtual (🤖) din colțul din dreapta jos
3. Testează funcționalitățile cu întrebări precum:
   - "Cum îmi îmbunătățesc EBITDA-ul?"
   - "Ce rating de credit am?"
   - "Cum optimizez fluxul de numerar?"

## 🎯 Funcționalități Principale

### Asistentul Virtual oferă:

- **Analiză EBITDA**: Recomandări pentru îmbunătățirea profitabilității
- **Evaluare Rating Credit**: Sfaturi pentru optimizarea scorului de credit
- **Optimizare Cash Flow**: Strategii pentru gestionarea fluxului de numerar
- **Planificare Investiții**: Recomandări de investiții cu ROI estimat
- **Gestionare Bugete**: Sfaturi pentru optimizarea structurii de costuri

### Caracteristici Tehnice:

- **Backend**: Flask cu API RESTful
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Responsive Design**: Adaptat pentru desktop și mobile
- **Real-time Chat**: Interfață de chat modernă și intuitivă
- **Offline Support**: Funcționare de bază chiar și fără server

## 📊 Indicatori Financiari Monitorizați

Asistentul analizează:
- Rata de lichiditate
- Raportul datorii/capitaluri proprii
- Marja de profit
- Fluxul de numerar
- Capacitatea de economisire

## 🔧 Personalizare

### Modificarea Datelor Companiei

În `app.py`, actualizează valorile din `company_data`:

```python
self.company_data = {
    'current_balance': 247856.45,      # Sold curent
    'monthly_revenue': 150000,         # Venit lunar
    'monthly_expenses': 120000,        # Cheltuieli lunare
    'employees_count': 24,             # Numărul de angajați
    'monthly_payroll': 89500,          # Masa salarială
    'debt_ratio': 0.3,                 # Raport datorii
    'liquidity_ratio': 1.8,            # Rata lichidității
    'profit_margin': 0.20,             # Marja de profit
    # ... alte valori
}
```

### Adăugarea de Sfaturi Noi

Extinde dicționarul `financial_tips` cu sfaturi personalizate:

```python
self.financial_tips = {
    'new_category': [
        "Sfat personalizat 1",
        "Sfat personalizat 2",
        # ...
    ]
}
```

## 🌐 API Endpoints

### POST `/api/chat`
Procesează mesajele utilizatorului și returnează răspunsuri inteligente.

**Request:**
```json
{
    "message": "Cum îmi îmbunătățesc EBITDA-ul?"
}
```

**Response:**
```json
{
    "success": true,
    "response": ["Răspuns structurat..."],
    "tips": ["Sfat 1", "Sfat 2"],
    "type": "ebitda",
    "timestamp": "2024-01-01T12:00:00"
}
```

### GET `/api/analysis`
Returnează o analiză completă a sănătății financiare.

### POST `/api/update_data`
Actualizează datele companiei pentru analize personalizate.

## 🎨 Personalizarea Interfeței

### Modificarea Culorilor Principale

În CSS, actualizează variabilele de culoare:

```css
:root {
    --primary-blue: #1e40af;
    --secondary-blue: #3b82f6;
    --accent-color: #10b981;
}
```

### Adăugarea de Animații

Toate animațiile sunt implementate cu CSS3 și JavaScript vanilla pentru performanță optimă.

## 🔍 Debugging și Troubleshooting

### Probleme Comune:

1. **Serverul nu pornește**: Verifică dacă toate dependențele sunt instalate
2. **CORS Error**: Asigură-te că Flask-CORS este configurat corect
3. **Chat nu funcționează**: Verifică consola browser-ului pentru erori JavaScript

### Logging:

Serverul afișează informații detaliate în consolă:
```
🚀 Starting BT-GO Virtual Assistant...
📊 Financial Advisory System Ready
🌐 Server running on http://localhost:5000
```

## 📱 Compatibilitate

- **Browsere**: Chrome, Firefox, Safari, Edge (versiuni moderne)
- **Dispozitive**: Desktop, tablet, smartphone
- **Rezoluții**: Responsive design pentru toate dimensiunile

## 🛡️ Securitate

- Validarea input-urilor utilizator
- Sanitizarea datelor financiare
- Protecție împotriva XSS și CSRF
- Rate limiting pe API endpoints

## 📈 Dezvoltare Viitoare

Funcționalități planificate:
- Integrare cu API-uri bancare reale
- Machine learning pentru predicții financiare
- Rapoarte PDF exportabile
- Notificări push pentru alerte financiare
- Integrare cu sisteme ERP

## 🤝 Contribuții

Pentru îmbunătățiri sau bug-uri, contactează echipa de dezvoltare.

## 📞 Support

Pentru suport tehnic sau întrebări, consultă documentația internă sau contactează echipa IT.

---

**Dezvoltat pentru BT-GO Business Banking Platform**  
*Asistent virtual inteligent pentru optimizarea performanței financiare*