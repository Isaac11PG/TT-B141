# TT-B141
# Cognitive Risk Estimation and Longitudinal Support System for Neurodegenerative Disease Screening (TT 2026-B141)

An end-to-end mobile and cloud-based clinical decision support system designed to assist healthcare professionals in the early detection and longitudinal monitoring of cognitive decline associated with neurodegenerative disorders, including Mild Cognitive Impairment (MCI), Alzheimer's Disease, and Vascular Dementia.

---

## 📌 Project Overview

Dementia affects over 55 million individuals globally, with late-stage diagnosis representing a major bottleneck due to manual assessment protocols and limited specialist availability. This project introduces an integrated mHealth platform that digitalizes the **Montreal Cognitive Assessment (MoCA)** test, couples assessment results with socio-demographic and lifestyle factors, and leverages supervised Machine Learning models to compute probabilistic risk profiles.

To bridge clinical adoption barriers and comply with ethical medical standards, the system incorporates **eXplainable Artificial Intelligence (XAI)** through SHAP (SHapley Additive exPlanations), providing medical practitioners with transparent, domain-level interpretability behind every prediction.

> **Disclaimer:** This software is designed strictly as a complementary clinical screening aid and probabilistic risk estimator. It does not provide definitive medical diagnoses or replace professional medical evaluation.

---

## 🏗 System Architecture & Key Features

- **Digital MoCA Assessment & Clinical Verification:** Structured interactive evaluations covering all core cognitive domains (visuospatial/executive, naming, memory, attention, language, abstraction, delayed recall, and orientation) secured with specialist verification tokens.
- **Multiclass Predictive Engine:** Supervised classifiers—Logistic Regression, Support Vector Machines (SVM), and Random Forest—trained on balanced clinical datasets using SMOTE (Synthetic Minority Over-sampling Technique) to prioritize diagnostic sensitivity and AUC-ROC.
- **Explainability Module (XAI):** Real-time feature contribution attribution using SHAP values to explain which cognitive domains or sociodemographic markers drove the risk score.
- **Longitudinal Tracking & Adaptive Cognitive Stimulation:** Patient progress visualization across consecutive sessions, automated regression alerts for clinical score drops ($\ge 3$ points), and personalized cognitive stimulation task recommendations prioritized by the patient's weakest domains.
- **Automated Clinical Reporting:** Generation of auditable, comprehensive PDF clinical reports including domain breakdown graphs, temporal progression trends, model confidence distributions, and mandatory non-diagnostic disclaimers.

---

## 💻 Tech Stack

- **Mobile Application (Frontend):** React Native (TypeScript), tailored for elderly accessibility, intuitive ergonomics, and low digital friction.
- **Backend Services & API:** Python, FastAPI (asynchronous REST architecture), SQLAlchemy ORM.
- **Machine Learning & Data Processing:** Scikit-Learn, Pandas, NumPy, Imbalanced-Learn (SMOTE), SHAP.
- **Reporting & Visualization:** ReportLab, Matplotlib, Seaborn.
- **Database & Persistence:** PostgreSQL, enforcing strict credential security (bcrypt with minimum work factor 12).
- **Cloud Infrastructure:** Microsoft Azure (App Service, Azure Database for PostgreSQL, Azure Blob Storage).

---

## 👥 Development Team

- **Institution:** Instituto Politécnico Nacional (IPN) — Escuela Superior de Cómputo (ESCOM)
- **Academic Degree:** B.S. in Computer Systems Engineering
- **Advising Director:** Dr. Rocío Palacios Solano
- **Authors / Developers:**
  - Isaac Pardo Gómez
  - Jonathan Ulises Rivera García
  - Iván Marcelino Meza Bravo 
