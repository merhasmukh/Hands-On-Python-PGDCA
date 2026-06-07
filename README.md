# Hands-On Python PGDCA

Welcome to the **Hands-On Python for PGDCA** course repository. This repository contains the complete curriculum, step-by-step practical Jupyter Notebooks, datasets, and standalone Python CLI/Streamlit applications designed to teach computer application students modern AI system integrations.

---

## 📂 Repository Structure

The course is structured into four core units, mapping from environment setup to deploying full-featured AI web applications:

### 📘 [Unit 1: Python Ecosystem for AI Applications](file:///Users/galaxyofai/Desktop/Github/Hands-On-Python-PGDCA/unit-1/)
Focuses on establishing virtual environments, basic data structures, exception handling, and data exploration.
* **Topics**: `venv` / `pip` setup, lists & dicts parser, custom helpers, `json` parsing, `os` / `pathlib`, and `pandas` data preparation.
* **Notebooks**: `01_python_installation_and_first_script.ipynb` through `11_unit_1_consolidation_data_prep_pipeline.ipynb`
* **Datasets**: Customer reviews CSV, nested API JSON outputs, sample article TXT.

### 📗 [Unit 2: API Integration & AI Service Consumption](file:///Users/galaxyofai/Desktop/Github/Hands-On-Python-PGDCA/unit-2/)
Focuses on connecting Python applications to Large Language Model (LLM) APIs securely and reliably.
* **Topics**: `requests` GET/POST, HTTP status validation, API key `.env` loading, retry backoff algorithms, `tiktoken` token estimators, and building reusable client modules.
* **Notebooks**: `12_requests_get_and_post.ipynb` through `22_unit_2_bonus_api_explorer_tool.ipynb`
* **Datasets**: Reference OpenAI/Anthropic completion payloads.

### 📙 [Unit 3: Building CLI Tools & AI Automation](file:///Users/galaxyofai/Desktop/Github/Hands-On-Python-PGDCA/unit-3/)
Focuses on creating command-line tools to process batch data and execute automation pipelines.
* **Topics**: `argparse` configuration, bulk text file globbing, template formatting, CLI output styling (progress indicators, tables), and automated test suites.
* **Notebooks**: `23_cli_arguments_sys_argv.ipynb` through `32_unit_3_consolidation_automation_suite.ipynb`
* **Features**: Standalone summarizer CLI, classifier CLI, debugging script workshop, and the `automation_suite` task modules.

### 📕 [Unit 4: AI Application Design & Deployment Basics](file:///Users/galaxyofai/Desktop/Github/Hands-On-Python-PGDCA/unit-4/)
Focuses on security auditing, system diagrams, Git workflows, and compiling interactive web application user interfaces.
* **Topics**: Redacting log keys, git commands, pandas-to-email report generation, and building functional Streamlit pages.
* **Notebooks**: `33_security_audit_and_hardening.ipynb` through `42_group_project_polish_and_presentation.ipynb`
* **Features**: Automated script security scanner, content generator, FAQ course database, and Streamlit app templates.

---

## 🛠️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/merhasmukh/Hands-On-Python-PGDCA.git
cd Hands-On-Python-PGDCA
```

### 2. Set up a Virtual Environment
Create and activate an isolated environment:
```bash
# Mac/Linux
python3 -m venv ai_env
source ai_env/bin/activate

# Windows
python -m venv ai_env
ai_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and supply your API configurations:
```env
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```
*(A default template is provided as `.env.example`)*

---

## 🖥️ Launching the Web Dashboards
To launch the Streamlit dashboards in Unit 4:
```bash
streamlit run unit-4/streamlit_apps/app_minimal.py
```