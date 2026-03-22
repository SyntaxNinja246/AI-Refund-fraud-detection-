
# Step 1: Import Required Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For model preparation later
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score

# Display settings
pd.set_option('display.max_columns', None)

# Step 2: Load the Dataset
df = pd.read_csv("Fraudulent_E-Commerce_Transaction_Data.csv")  # <-- replace with your actual file name
print("Shape:", df.shape)
print("\nPreview:")
print(df.head())


# ---------------------Step 2: Basic Data Audit-------------------------------------------

# Check missing values
print("Missing values per column:\n", df.isnull().sum())

# Check duplicates
print("\nDuplicate rows:", df.duplicated().sum())

# Fraud distribution
fraud_counts = df['Is Fraudulent'].value_counts()
fraud_percentage = df['Is Fraudulent'].value_counts(normalize=True) * 100
print("\nFraud distribution:\n", fraud_counts)
print("\nFraud percentage:\n", fraud_percentage)

# Quick statistics
print("\nTransaction Amount Summary:\n", df['Transaction Amount'].describe())
print("\nCustomer Age Summary:\n", df['Customer Age'].describe())
print("\nAccount Age (Days) Summary:\n", df['Account Age Days'].describe())


plt.figure(figsize=(8,10))
sns.countplot(x='Is Fraudulent', data=df, palette='viridis')
plt.title("Fraud vs Non-Fraud Transactions")
plt.show()

# ========================================
# ✨ EDA VISUALIZATIONS ✨
# ========================================

import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

# Style setup
sns.set_theme(style="whitegrid", palette="coolwarm")
plt.rcParams['figure.facecolor'] = "#9465ed"
plt.rcParams['axes.facecolor'] = "#4c14d9"
plt.rcParams['axes.edgecolor'] = "#efef76"
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.titlepad'] = 15
plt.rcParams['font.size'] = 12

# Helper function to show nicer countplots
def pretty_countplot(x, hue, data, title, rotation=0, figsize=(7,5)):
    plt.figure(figsize=figsize)
    ax = sns.countplot(x=x, hue=hue, data=data, edgecolor='black', alpha=0.8)
    plt.title(title, fontsize=13, weight='bold')
    plt.xlabel(x.replace('_', ' ').title())
    plt.ylabel("Transaction Count")
    plt.xticks(rotation=rotation)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.legend(title="Is Fraudulent", loc="upper right", labels=["No", "Yes"])
    plt.tight_layout()
    plt.show()

# 1️⃣ Fraud vs Transaction Amount
plt.figure(figsize=(7,5))
sns.boxplot(
    x='Is Fraudulent', y='Transaction Amount', data=df,
    palette=["#DBF703", "#08E0B9"], linewidth=1.8, fliersize=3, width=0.9
)
plt.title("Transaction Amount Distribution by Fraud Status", fontsize=13, weight='bold')
plt.xlabel("Fraudulent?")
plt.ylabel("Transaction Amount ($)")
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

##THEME SET UP FOR PAYMENT OPTION AND DEVICE USED
# --- Theme Setup ---
sns.set_theme(style="whitegrid")
plt.rcParams['figure.facecolor'] = '#0D1117'   # dark navy background
plt.rcParams['axes.facecolor'] = '#161B22'     # slightly lighter inner area
plt.rcParams['axes.edgecolor'] = '#30363D'
plt.rcParams['text.color'] = '#C9D1D9'
plt.rcParams['axes.labelcolor'] = '#C9D1D9'
plt.rcParams['xtick.color'] = '#C9D1D9'
plt.rcParams['ytick.color'] = '#C9D1D9'
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11


# Compute fraud share by payment method
fraud_rate_by_payment = df.groupby('Payment Method')['Is Fraudulent'].mean().sort_values(ascending=False)

colors = sns.color_palette("coolwarm", len(fraud_rate_by_payment))
fig, ax = plt.subplots(figsize=(7,7), facecolor='#0D1117')

wedges, texts, autotexts = ax.pie(
    fraud_rate_by_payment,
    labels=fraud_rate_by_payment.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    textprops={'color': 'white', 'fontsize': 11},
    wedgeprops={'edgecolor': '#0D1117', 'linewidth': 2},
    pctdistance=0.75,     # move % labels inside the donut
    labeldistance=1.05
)

# Add circle in center to make it donut
centre_circle = plt.Circle((0,0),0.60,fc='#0D1117')
fig.gca().add_artist(centre_circle)

plt.title('Average Fraud Rate by Payment Method', fontsize=14, color='#F0F6FC', weight='bold', pad=0)
plt.tight_layout()
plt.show()


# Fraud rate by device
fraud_rate_by_device = df.groupby('Device Used')['Is Fraudulent'].mean().sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(7,5), facecolor='#0D1117')
bars = ax.barh(
    fraud_rate_by_device.index,
    fraud_rate_by_device.values,
    color=sns.color_palette("flare", len(fraud_rate_by_device)),
    edgecolor='white',
    linewidth=1.2,
    alpha=0.9
)

import matplotlib as mpl
ax.set_title("Fraud Rate by Device Type", fontsize=14, color='#F0F6FC', weight='bold', pad=15)
ax.set_xlabel("Fraud Rate (%)", color='#C9D1D9', fontsize=11)
ax.set_ylabel("")
ax.xaxis.set_major_formatter(mpl.ticker.PercentFormatter(1)) # type: ignore
ax.grid(axis='x', linestyle='--', alpha=0.2)

# Subtle glow effect (by re-plotting lighter bars)
for bar in bars:
    ax.barh(
        [bar.get_y() + bar.get_height()/2],
        [bar.get_width()],
        height=bar.get_height()*1.3,
        color=bar.get_facecolor(),
        alpha=0.15,
        zorder=-1
    )

fig.patch.set_facecolor("#031F72")
ax.set_facecolor("#52F5F5")

plt.tight_layout()
plt.show()



# 4️⃣ Product Category
top_categories = df['Product Category'].value_counts().nlargest(10).index
plt.rcParams['figure.facecolor'] = "#5B94EA"   # deep dark navy
plt.rcParams['axes.facecolor'] = "#000000"     # slightly lighter dark
plt.rcParams['axes.edgecolor'] = "#000000"
plt.rcParams['text.color'] = "#FFFFFF"
plt.rcParams['axes.labelcolor'] = "#EFE82F"
plt.rcParams['xtick.color'] = '#C9D1D9'
plt.rcParams['ytick.color'] = "#EC3C44"
pretty_countplot('Product Category', 'Is Fraudulent',
                 df[df['Product Category'].isin(top_categories)],
                 "Fraud Frequency by Top 10 Product Categories", rotation=30, figsize=(9,5))

# 5️⃣ Fraud vs Transaction Hour
plt.figure(figsize=(9,5))
sns.histplot(
    data=df, x='Transaction Hour', hue='Is Fraudulent', multiple='stack',
    bins=24, palette=['#4F8BD7', '#E63946'], alpha=0.85, edgecolor='blue'
)
plt.title("Fraud Occurrence by Transaction Hour", fontsize=17, weight='bold')
plt.xlabel("Hour of Day")
plt.ylabel("Transaction Count")
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()

# 6️⃣ Correlation Heatmap
plt.figure(figsize=(8,6))
plt.rcParams['figure.facecolor'] = "#225971" 
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='RdBu_r', center=0, fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap", fontsize=13, weight='bold')
plt.tight_layout()
plt.show()

#🧩 Step 4 — Feature Engineering

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Copy dataset
data = df.copy()

# 1️⃣ Encode categorical features
categorical_cols = ['Payment Method', 'Product Category', 'Device Used', 
                    'Customer Location', 'Shipping Address', 'Billing Address']

le = LabelEncoder()
for col in categorical_cols:
    data[col] = le.fit_transform(data[col])

# 2️⃣ Feature-target split
X = data.drop(['Is Fraudulent', 'Transaction ID', 'Customer ID', 'IP Address', 'Transaction Date'], axis=1)
y = data['Is Fraudulent']

# 3️⃣ Scale numeric features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4️⃣ Train-test split (stratified because fraud = rare)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, stratify=y, random_state=42
)

print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")
print(f"Fraud in train: {y_train.mean()*100:.2f}%, Fraud in test: {y_test.mean()*100:.2f}%")

#🚀 ---------------------------------— Model Training & Evaluation (Supervised)-----------------------------------------
#We’ll start with two strong baseline models:
#🌲 Random Forest Classifier
#⚡ XGBoost Classifier

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report
import pandas as pd

# Helper function to evaluate models
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:,1] if hasattr(model, "predict_proba") else None

    metrics = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred),
        'Recall': recall_score(y_test, y_pred),
        'F1-Score': f1_score(y_test, y_pred),
        'ROC-AUC': roc_auc_score(y_test, y_proba) if y_proba is not None else None
    }
    return pd.Series(metrics)

# 1️⃣ Random Forest
rf = RandomForestClassifier(n_estimators=200, random_state=42, class_weight='balanced', n_jobs=-1)
rf.fit(X_train, y_train)
rf_results = evaluate_model(rf, X_test, y_test)
print("\n🌲 Random Forest Results:")
print(rf_results)

# 2️⃣ XGBoost
xgb = XGBClassifier(
    n_estimators=300,
    learning_rate=0.1,
    max_depth=8,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    scale_pos_weight=(1 / y_train.mean()),  # handles imbalance
    eval_metric='logloss',
    use_label_encoder=False
)
xgb.fit(X_train, y_train)
xgb_results = evaluate_model(xgb, X_test, y_test)
print("\n⚡ XGBoost Results:")
print(xgb_results)

# Compare
comparison = pd.DataFrame({'Random Forest': rf_results, 'XGBoost': xgb_results})
print("\n📊 Model Comparison:\n", comparison)

#⚡---------------------------------------------- Step 5 — Train and Compare Models-----------------------------

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import pandas as pd

# Helper function to evaluate models
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None

    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1-Score": f1_score(y_test, y_pred),
        "ROC-AUC": roc_auc_score(y_test, y_proba) if y_proba is not None else None,
    }
    return pd.Series(metrics)

# 🌲 Random Forest Model


import time
print("🚀 Training Random Forest Model...")
start_time = time.time()
rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight='balanced',
    n_jobs=-1
)
rf.fit(X_train, y_train)
print(f"✅ Random Forest trained successfully in {time.time() - start_time:.2f} seconds.\n")

rf_results = evaluate_model(rf, X_test, y_test)
print("🌲 Random Forest Results:\n", rf_results)


# ⚡ XGBOOST MODEL
print("🚀 Training XGBoost Model...")
start_time = time.time()
xgb = XGBClassifier(
    n_estimators=300,
    learning_rate=0.1,
    max_depth=8,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    scale_pos_weight=(1 / y_train.mean()),  # handles imbalance
    eval_metric='logloss',
    use_label_encoder=False
)
xgb.fit(X_train, y_train)
print(f"✅ XGBoost trained successfully in {time.time() - start_time:.2f} seconds.\n")

xgb_results = evaluate_model(xgb, X_test, y_test)
print("⚡ XGBoost Results:\n", xgb_results)


# 📊 COMPARE MODELS
comparison = pd.DataFrame({'Random Forest': rf_results, 'XGBoost': xgb_results})
print("\n📊 Model Comparison:\n", comparison)

#🧩 Step 6 — Model Interpretation & Visualization
#📊 Visualize feature importance (which features most influence fraud detection).
#🎯 Plot ROC Curve (model discrimination ability).
#⚖️ Plot Precision–Recall Curve (see trade-off between catching frauds and false alarms).

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, precision_recall_curve, roc_auc_score
import numpy as np

# Global dark theme 🎨
plt.style.use('dark_background')
sns.set_style("whitegrid", {'axes.facecolor': '#0c0f1a', 'grid.color': '#1c1f2b'})
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#2e3357'
plt.rcParams['axes.labelcolor'] = '#b6b6c9'
plt.rcParams['xtick.color'] = '#b6b6c9'
plt.rcParams['ytick.color'] = '#b6b6c9'
plt.rcParams['figure.facecolor'] = '#0c0f1a'

# ======================
# 1️⃣ FEATURE IMPORTANCE
# ======================

def futuristic_barplot(importances, title, cmap):
    colors = sns.color_palette(cmap, len(importances))
    fig, ax = plt.subplots(figsize=(9,5))
    bars = sns.barplot(
        x=importances.values[:10],
        y=importances.index[:10],
        palette=colors,
        ax=ax
    )
    ax.set_title(title, fontsize=16, color='#7ee6fd', weight='bold', pad=20)
    ax.set_xlabel("Importance Score", fontsize=12, color='#a1a4b2')
    ax.set_ylabel("")
    for spine in ax.spines.values():
        spine.set_visible(False)
    for i, v in enumerate(importances.values[:10]):
        ax.text(v + 0.002, i, f"{v:.3f}", color="#7ee6fd", fontsize=10, va='center')
    plt.tight_layout()
    plt.show()

# Random Forest
rf_importance = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
futuristic_barplot(rf_importance, "Top 10 Important Features — Random Forest", "mako")

# XGBoost
xgb_importance = pd.Series(xgb.feature_importances_, index=X.columns).sort_values(ascending=False)
futuristic_barplot(xgb_importance, "Top 10 Important Features — XGBoost", "rocket_r")

# ======================
# 2️⃣ ROC CURVE
# ======================

y_proba_rf = rf.predict_proba(X_test)[:, 1]
y_proba_xgb = xgb.predict_proba(X_test)[:, 1]

fpr_rf, tpr_rf, _ = roc_curve(y_test, y_proba_rf)
fpr_xgb, tpr_xgb, _ = roc_curve(y_test, y_proba_xgb)

y_pred_rf = (y_proba_rf >= 0.5).astype(int)
y_pred_xgb = (y_proba_xgb >= 0.5).astype(int)



plt.figure(figsize=(8,6))
plt.plot(fpr_rf, tpr_rf, color="#5ef1d3", lw=2.5, label=f"Random Forest (AUC={roc_auc_score(y_test, y_proba_rf):.3f})")
plt.plot(fpr_xgb, tpr_xgb, color="#e273ff", lw=2.5, label=f"XGBoost (AUC={roc_auc_score(y_test, y_proba_xgb):.3f})")
plt.plot([0,1],[0,1],'--',color='#44475a')
plt.title("ROC Curve — Fraud Detection", fontsize=16, color='#7ee6fd', weight='bold', pad=20)
plt.xlabel("False Positive Rate", color='#b6b6c9')
plt.ylabel("True Positive Rate", color='#b6b6c9')
plt.legend(frameon=False, loc='lower right', fontsize=10)
plt.grid(alpha=0.15)
plt.tight_layout()
plt.show()

# ======================
# 3️⃣ PRECISION–RECALL
# ======================

prec_rf, rec_rf, _ = precision_recall_curve(y_test, y_proba_rf)
prec_xgb, rec_xgb, _ = precision_recall_curve(y_test, y_proba_xgb)

plt.figure(figsize=(8,6))
plt.plot(rec_rf, prec_rf, color="#5ef1d3", lw=2.5, label="Random Forest")
plt.plot(rec_xgb, prec_xgb, color="#e273ff", lw=2.5, label="XGBoost")
plt.fill_between(rec_rf, prec_rf, color="#5ef1d3", alpha=0.15)
plt.fill_between(rec_xgb, prec_xgb, color="#e273ff", alpha=0.15)
plt.title("⚖️ Precision–Recall Curve", fontsize=16, color='#7ee6fd', weight='bold', pad=20)
plt.xlabel("Recall", color='#b6b6c9')
plt.ylabel("Precision", color='#b6b6c9')
plt.legend(frameon=False, fontsize=10)
plt.grid(alpha=0.15)
plt.tight_layout()
plt.show()

import pandas as pd

final_results = pd.DataFrame(X_test, columns=X.columns)

final_results['Actual'] = y_test
final_results['Predicted'] = y_pred_xgb

final_results.to_csv("fraud_detection_results.csv", index=False)




