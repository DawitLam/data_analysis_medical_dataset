# Healthcare Data Analysis Portfolio

## Overview
End-to-end healthcare data analysis demonstrating comprehensive data science skills applied to synthetic medical data. This project showcases real-world analytical workflows from data quality assessment through advanced modeling and interpretation.

## Key Skills Demonstrated
- **Data Quality Management**: Controlled injection and remediation of missing data and duplicates
- **Feature Engineering**: Clinical data transformation including heart rate variability, lab aggregates, and temporal features
- **Machine Learning**: Complication prediction with proper handling of class imbalance
- **Data Leakage Prevention**: Rigorous separation of target variables from feature sets
- **Healthcare Domain Knowledge**: Clinical insight interpretation and realistic modeling approaches
- **Professional Code Organization**: Modular cells, consolidated imports, and comprehensive documentation

## Technical Highlights
- **Data Cleaning**: Multiple imputation strategies (mode, median, KNN)
- **Feature Engineering**: 28+ engineered features including temporal patterns and clinical aggregates
- **Model Evaluation**: ROC/PR curves, confusion matrices, feature importance analysis
- **Class Imbalance**: Balanced sampling and threshold optimization techniques
- **Visualization**: Publication-ready plots for stakeholder communication

## Technologies Used
- **Python**: pandas, numpy, scikit-learn, matplotlib, seaborn
- **Machine Learning**: Logistic Regression, Random Forest, XGBoost
- **Statistical Analysis**: scipy, statsmodels
- **Development Environment**: Jupyter Notebook for reproducible analysis

## Project Structure
```
healthcare-analysis-portfolio/
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
├── generate_data.py                    # Synthetic data generation
├── notebooks/
│   └── healthcare_analysis_portfolio.ipynb  # Main analysis notebook
└── .gitignore                         # Git ignore rules
```

## How to Run
1. **Install dependencies**: 
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate synthetic data**:
   ```bash
   python generate_data.py
   ```

3. **Run analysis**:
   Open `notebooks/healthcare_analysis_portfolio.ipynb` in Jupyter and run all cells

## Key Findings
- **Class Imbalance**: 14% complication rate reflects realistic clinical scenarios
- **Model Performance**: Balanced models achieve 65% accuracy with 25% recall for minority class detection
- **Feature Importance**: Heart rate variability and lab values show strongest predictive signal
- **Data Quality**: Demonstrates robust handling of 5% missing ethnicity data and 15 missing heart rate values

## Business Impact
This analysis framework can be applied to:
- **Clinical Risk Assessment**: Early identification of patients at risk for complications
- **Resource Planning**: Prediction of high-utilization patients for capacity management
- **Quality Improvement**: Data-driven insights for reducing procedure complications

## Data Privacy
All data in this project is synthetically generated and contains no real patient information. The analysis demonstrates healthcare data science techniques while maintaining complete privacy compliance.

## Next Steps
- **Enhanced Feature Engineering**: Incorporate temporal patterns and interaction effects
- **Advanced Sampling**: Implement SMOTE/ADASYN for minority class augmentation
- **Cost-Sensitive Learning**: Optimize for clinical risk tolerance
- **Ensemble Methods**: Combine multiple approaches for robust predictions
- **Domain Expert Integration**: Include clinical knowledge in feature selection

---

*This project demonstrates advanced healthcare data science capabilities with a focus on real-world applicability, ethical considerations, and professional code quality.*